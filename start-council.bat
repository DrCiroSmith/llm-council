@echo off
REM ============================================
REM  LLM Council - Always-Live Service Launcher
REM  Port: 8002 | Leviathan Ecosystem Service
REM ============================================

title LLM Council Backend [Port 8002]

cd /d "%~dp0"

:start_loop
echo [%date% %time%] Starting LLM Council backend on port 8002...
python -m backend.main
echo [%date% %time%] Backend exited. Restarting in 5 seconds...
timeout /t 5 /nobreak >nul
goto start_loop
