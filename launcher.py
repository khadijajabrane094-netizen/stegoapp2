# launcher.py
import os
import sys
import subprocess
import webbrowser
import time
import socket

def find_free_port():
    """Trouver un port libre"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def run_app():
    """Lancer l'application"""
    port = find_free_port()
    
    print("=" * 50)
    print("   🛡️ StegoApp - Lancement")
    print("=" * 50)
    print("⏳ Démarrage de l'application...")
    
    # Lancer Streamlit
    process = subprocess.Popen([
        sys.executable,
        "-m", "streamlit", "run",
        "app.py",
        "--server.port", str(port),
        "--server.headless", "true",
        "--browser.serverAddress", "localhost"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    time.sleep(3)
    webbrowser.open(f"http://localhost:{port}")
    
    print(f"✅ Application lancée sur: http://localhost:{port}")
    print("💡 Appuyez sur CTRL+C pour fermer")
    print("=" * 50)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🔴 Arrêt de l'application...")
        process.terminate()
        sys.exit(0)

if __name__ == "__main__":
    run_app()