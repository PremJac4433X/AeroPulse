@echo off
title AeroPulse GitHub Deployer
color 0A
cd /d "%~dp0"
echo ================================================================
echo   AEROPULSE: PUSHING TO GITHUB (priyu210824/AeroPulse)
echo ================================================================
echo.
git push -u origin main
echo.
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Code pushed to GitHub successfully!
    echo.
    echo Now open Render to deploy: https://dashboard.render.com
) else (
    echo [NOTE] If a browser login window appears, please authorize your GitHub account.
)
echo.
pause
