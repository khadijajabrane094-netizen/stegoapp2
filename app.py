from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
import time
import base64
import os

st.set_page_config(
    page_title="🛡️ StegoApp Premium",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# ===== خلفية رائعة جداً =====
# ============================================================

background_url = "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1920"

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{background_url}") no-repeat center center fixed !important;
        background-size: cover !important;
    }}
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.65);
        z-index: 0;
    }}
    .stApp > div {{
        position: relative;
        z-index: 1;
    }}
    .block-container {{
        background: transparent !important;
        padding-top: 20px !important;
        padding-bottom: 20px !important;
    }}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Style pour les scrollbars */
    ::-webkit-scrollbar {{
        width: 6px;
    }}
    ::-webkit-scrollbar-track {{
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }}
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(180deg, #1DB954, #1ed760);
        border-radius: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# ===== دوال الستيغانوغرافيا =====
# ============================================================

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_data):
    parts = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    text = ""
    for part in parts:
        if len(part) == 8:
            text += chr(int(part, 2))
    return text

def encode_image(pil_img, secret_text):
    img = pil_img.convert('RGB')
    pixels = img.load()
    binary_secret = text_to_binary(secret_text + "$$$")
    data_index = 0
    data_len = len(binary_secret)
    width, height = img.size
    
    max_chars = (width * height * 3) // 8 - 3
    if len(secret_text) > max_chars:
        raise ValueError(f"⚠️ Message trop long! Max: {max_chars} caractères")
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if data_index < data_len:
                r = (r & 254) | int(binary_secret[data_index])
                data_index += 1
            if data_index < data_len:
                g = (g & 254) | int(binary_secret[data_index])
                data_index += 1
            if data_index < data_len:
                b = (b & 254) | int(binary_secret[data_index])
                data_index += 1
            pixels[x, y] = (r, g, b)
            if data_index >= data_len: break
        if data_index >= data_len: break
    return img

def decode_image(pil_img):
    pixels = pil_img.load()
    binary_data = ""
    width, height = pil_img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)
    full_text = binary_to_text(binary_data)
    if "$$$" in full_text:
        return full_text.split("$$$")[0]
    return None

# ============================================================
# ===== CSS Design Nadya =====
# ============================================================

st.markdown("""
<style>
/* ===== DESIGN GLOBAL ===== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* ===== HEADER PREMIUM ===== */
.premium-header {
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(30px);
    -webkit-backdrop-filter: blur(30px);
    border-radius: 28px;
    padding: 30px 40px;
    margin-bottom: 24px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 8px 40px rgba(0, 0, 0, 0.4);
    animation: fadeInDown 0.8s ease-out;
}

.premium-header .icon {
    font-size: 52px;
    display: block;
    margin-bottom: 8px;
}

.premium-header .title {
    font-size: 38px;
    font-weight: 800;
    background: linear-gradient(135deg, #1DB954, #1ed760, #00d4ff, #a855f7);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientShift 4s ease-in-out infinite;
    margin: 0;
    letter-spacing: -0.5px;
}

.premium-header .subtitle {
    color: rgba(255, 255, 255, 0.4);
    font-size: 14px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 6px;
    font-weight: 300;
}

/* ===== ANIMATIONS ===== */
@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

@keyframes pulse {
    0% { box-shadow: 0 0 20px rgba(29, 185, 84, 0.2); }
    50% { box-shadow: 0 0 40px rgba(29, 185, 84, 0.4); }
    100% { box-shadow: 0 0 20px rgba(29, 185, 84, 0.2); }
}

/* ===== CARDS PREMIUM ===== */
.premium-card {
    background: rgba(255, 255, 255, 0.04);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 28px;
    margin-bottom: 18px;
    border: 1px solid rgba(255, 255, 255, 0.06);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    animation: fadeInDown 0.6s ease-out;
}

.premium-card:hover {
    background: rgba(255, 255, 255, 0.07);
    border-color: rgba(29, 185, 84, 0.2);
    transform: translateY(-4px);
    box-shadow: 0 8px 50px rgba(0, 0, 0, 0.3);
}

.premium-card .card-icon {
    font-size: 28px;
    margin-right: 12px;
}

.premium-card .card-title {
    font-size: 18px;
    font-weight: 700;
    color: #1DB954;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.premium-card .card-desc {
    color: rgba(255, 255, 255, 0.4);
    font-size: 14px;
    margin-bottom: 12px;
}

/* ===== BOUTONS PREMIUM ===== */
.btn-premium {
    background: linear-gradient(135deg, #1DB954, #1ed760);
    color: #000000 !important;
    border: none;
    padding: 16px 32px;
    border-radius: 50px;
    font-weight: 700;
    font-size: 16px;
    width: 100%;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 30px rgba(29, 185, 84, 0.25);
    animation: pulse 3s ease-in-out infinite;
}

.btn-premium:hover {
    transform: scale(1.03) !important;
    box-shadow: 0 8px 40px rgba(29, 185, 84, 0.4) !important;
}

.btn-premium:active {
    transform: scale(0.97) !important;
}

.btn-premium-secondary {
    background: rgba(255, 255, 255, 0.08);
    color: #ffffff !important;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 14px 28px;
    border-radius: 50px;
    font-weight: 600;
    font-size: 15px;
    width: 100%;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-premium-secondary:hover {
    background: rgba(255, 255, 255, 0.14);
    border-color: rgba(255, 255, 255, 0.2);
}

/* ===== STREAMLIT STYLING ===== */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 6px;
    backdrop-filter: blur(10px);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 12px;
    padding: 12px 28px;
    font-weight: 600;
    font-size: 14px;
    color: rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    background: transparent;
}

.stTabs [data-baseweb="tab"]:hover {
    color: rgba(255, 255, 255, 0.8);
}

.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background: linear-gradient(135deg, #1DB954, #1ed760);
    color: #000000 !important;
    box-shadow: 0 4px 20px rgba(29, 185, 84, 0.2);
}

.stButton button {
    background: linear-gradient(135deg, #1DB954, #1ed760) !important;
    color: #000000 !important;
    border: none !important;
    border-radius: 16px !important;
    padding: 16px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 25px rgba(29, 185, 84, 0.15) !important;
}

.stButton button:hover {
    transform: scale(1.03) !important;
    box-shadow: 0 8px 35px rgba(29, 185, 84, 0.3) !important;
}

.stFileUploader {
    border: 2px dashed rgba(29, 185, 84, 0.2) !important;
    border-radius: 18px !important;
    background: rgba(255, 255, 255, 0.02) !important;
    transition: all 0.3s ease !important;
    padding: 10px !important;
}

.stFileUploader:hover {
    border-color: rgba(29, 185, 84, 0.5) !important;
    background: rgba(29, 185, 84, 0.04) !important;
}

.stImage img {
    border-radius: 18px !important;
    box-shadow: 0 8px 40px rgba(0, 0, 0, 0.5) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
}

.stSuccess {
    border-left: 4px solid #1DB954 !important;
    background: rgba(29, 185, 84, 0.08) !important;
    border-radius: 14px !important;
    backdrop-filter: blur(10px) !important;
}

.stError {
    border-left: 4px solid #ef4444 !important;
    background: rgba(239, 68, 68, 0.08) !important;
    border-radius: 14px !important;
    backdrop-filter: blur(10px) !important;
}

.stWarning {
    border-left: 4px solid #f59e0b !important;
    background: rgba(245, 158, 11, 0.08) !important;
    border-radius: 14px !important;
    backdrop-filter: blur(10px) !important;
}

.stSpinner {
    color: #1DB954 !important;
}

/* ===== FOOTER ===== */
.premium-footer {
    text-align: center;
    color: rgba(255, 255, 255, 0.12);
    font-size: 12px;
    padding: 20px 0;
    margin-top: 30px;
    border-top: 1px solid rgba(255, 255, 255, 0.03);
    letter-spacing: 1px;
}

/* ===== RESPONSIVE ===== */
@media (max-width: 600px) {
    .premium-header {
        padding: 20px;
    }
    .premium-header .title {
        font-size: 28px;
    }
    .premium-header .icon {
        font-size: 40px;
    }
    .premium-card {
        padding: 18px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 16px;
        font-size: 12px;
    }
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# ===== HEADER =====
# ============================================================

st.markdown("""
<div class="premium-header">
    <span class="icon">🛡️</span>
    <h1 class="title">StegoApp Premium</h1>
    <p class="subtitle">⚡ Système de Stéganographie LSB — Sécurité & Innovation</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# ===== Interface =====
# ============================================================

tab1, tab2 = st.tabs(["🔒 Cacher un Message", "🔓 Extraire un Message"])

with tab1:
    st.markdown("""
    <div class="premium-card">
        <div class="card-title">
            <span class="card-icon">📤</span> Téléchargez votre image
        </div>
        <p class="card-desc">Formats supportés: JPG, JPEG, PNG</p>
    </div>
    """, unsafe_allow_html=True)
    
    fichier = st.file_uploader("", type=["jpg", "jpeg", "png"], key="enc", label_visibility="collapsed")
    
    if fichier:
        img = Image.open(fichier)
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(img, width=200)
        with col2:
            st.markdown(f"**📐 Dimensions:** {img.size[0]} x {img.size[1]}")
            max_car = (img.size[0] * img.size[1] * 3) // 8 - 3
            st.markdown(f"**✏️ Capacité max:** {max_car} caractères")
        
        texte = st.text_area("💬 Message secret:", placeholder="Tapez votre message ici...")
        
        if st.button("🔒 Cacher le message", use_container_width=True):
            if texte:
                try:
                    with st.spinner("⏳ Encodage en cours..."):
                        img_encoded = encode_image(img, texte)
                        img_encoded.save("stego_output.png", "PNG")
                    st.success("✅ Message caché avec succès!")
                    with open("stego_output.png", "rb") as f:
                        st.download_button(
                            "📥 Télécharger l'image",
                            data=f,
                            file_name="stego_image.png",
                            mime="image/png",
                            use_container_width=True
                        )
                except Exception as e:
                    st.error(str(e))
            else:
                st.warning("⚠️ Entrez un message!")

with tab2:
    st.markdown("""
    <div class="premium-card">
        <div class="card-title">
            <span class="card-icon">🔍</span> Extraire le message
        </div>
        <p class="card-desc">Téléchargez l'image stéganographiée (PNG)</p>
    </div>
    """, unsafe_allow_html=True)
    
    fichier_stego = st.file_uploader("", type=["png"], key="dec", label_visibility="collapsed")
    
    if fichier_stego:
        img_stego = Image.open(fichier_stego)
        st.image(img_stego, width=200)
        
        if st.button("🔓 Extraire le message", use_container_width=True):
            with st.spinner("⏳ Extraction..."):
                time.sleep(0.5)
                result = decode_image(img_stego)
                if result:
                    st.success(f"📩 Message: **{result}**")
                else:
                    st.error("❌ Aucun message caché trouvé!")

# ============================================================
# ===== FOOTER =====
# ============================================================

st.markdown("""
<div class="premium-footer">
    🛡️ StegoApp Premium v3.0 — Projet de Soutenance 2026
</div>
""", unsafe_allow_html=True)