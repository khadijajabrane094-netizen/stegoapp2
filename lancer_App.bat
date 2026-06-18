@echo off
title 🛡️ StegoApp Premium
color 0A
echo ============================================
echo    🛡️ StegoApp Premium v3.0
echo    Système de Stéganographie LSB
echo ============================================
echo.
echo ⏳ Démarrage de l'application...
echo.
cd /d "%~dp0"
python -m streamlit run app.py --server.port 8501
pause