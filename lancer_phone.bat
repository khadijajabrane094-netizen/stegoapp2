@echo off
title 📱 StegoApp - Mode Téléphone
color 0E
echo ============================================
echo    📱 StegoApp - Mode Téléphone
echo ============================================
echo.
echo ⏳ Démarrage du serveur...
echo.
cd /d "%~dp0"
python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
echo.
echo ============================================
echo    ✅ Serveur lancé!
echo    📱 Ouvrez sur votre téléphone:
echo    http://[VOTRE_IP]:8501
echo ============================================
pause