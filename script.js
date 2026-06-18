// script.js - Design Nadya

document.addEventListener("DOMContentLoaded", function() {
    
    // ===== Bouton principal =====
    var button = document.getElementById('btn-interactif');
    
    if (button) {
        button.addEventListener('click', function(event) {
            // Effet de clic
            this.innerHTML = '⚡ Protocol Initialisé avec Succès !';
            this.style.background = 'linear-gradient(135deg, #00d4ff, #a855f7)';
            this.style.transform = 'scale(0.95)';
            this.style.boxShadow = '0 0 60px rgba(0, 212, 255, 0.4)';
            
            // Retour à l'état normal
            setTimeout(function() {
                button.innerHTML = '🔒 Initialiser le Protocol';
                button.style.background = 'linear-gradient(135deg, #1DB954, #1ed760)';
                button.style.transform = 'scale(1)';
                button.style.boxShadow = '0 4px 30px rgba(29, 185, 84, 0.25)';
            }, 2500);
        });
    }
    
    // ===== Effet de particules sur le logo =====
    var header = document.querySelector('.premium-header');
    if (header) {
        header.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.5s ease';
            this.style.transform = 'scale(1.02)';
            this.style.boxShadow = '0 12px 60px rgba(0,0,0,0.5)';
        });
        
        header.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
            this.style.boxShadow = '0 8px 40px rgba(0,0,0,0.4)';
        });
    }
    
    // ===== Animation des cartes =====
    var cards = document.querySelectorAll('.premium-card');
    cards.forEach(function(card, index) {
        card.style.animationDelay = (index * 0.2) + 's';
    });
    
    // ===== Horloge en direct =====
    function updateClock() {
        var now = new Date();
        var hours = String(now.getHours()).padStart(2, '0');
        var minutes = String(now.getMinutes()).padStart(2, '0');
        var seconds = String(now.getSeconds()).padStart(2, '0');
        
        var clockElement = document.getElementById('live-clock');
        if (clockElement) {
            clockElement.textContent = hours + ':' + minutes + ':' + seconds;
        }
    }
    
    // ===== Créer l'horloge =====
    var footer = document.querySelector('.premium-footer');
    if (footer) {
        var clock = document.createElement('span');
        clock.id = 'live-clock';
        clock.style.cssText = 'display: block; margin-top: 8px; font-family: monospace; font-size: 14px; color: rgba(255,255,255,0.2);';
        footer.appendChild(clock);
        setInterval(updateClock, 1000);
        updateClock();
    }
    
    // ===== Effet de particules en arrière-plan =====
    function createParticles() {
        const particlesContainer = document.createElement('div');
        particlesContainer.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
            overflow: hidden;
        `;
        document.body.appendChild(particlesContainer);
        
        for (let i = 0; i < 30; i++) {
            const particle = document.createElement('div');
            const size = Math.random() * 3 + 1;
            particle.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                background: rgba(29, 185, 84, ${Math.random() * 0.2 + 0.05});
                border-radius: 50%;
                top: ${Math.random() * 100}%;
                left: ${Math.random() * 100}%;
                animation: floatParticle ${Math.random() * 20 + 10}s linear infinite;
                animation-delay: ${Math.random() * 10}s;
            `;
            particlesContainer.appendChild(particle);
        }
    }
    
    // ===== Animation des particules =====
    const styleSheet = document.createElement("style");
    styleSheet.textContent = `
        @keyframes floatParticle {
            0% {
                transform: translateY(0) translateX(0);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateY(-100vh) translateX(${Math.random() * 100 - 50}px);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(styleSheet);
    
    // Lancer les particules (désactivé pour performance)
    // createParticles();
    
    console.log("🛡️ StegoApp Premium - Design Nadya");
    console.log("⚡ Système de Stéganographie LSB");
});