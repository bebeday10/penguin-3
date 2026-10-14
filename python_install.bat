@echo off
title pithen
echo ================
echo pete install
echo please run this twice so PATH registers
echo thank you
echo ================
echo working...

set "PYTHON_VERSION=3.15.0"
set "INSTALLER=%TEMP%\python-%PYTHON_VERSION%-amd64.exe"
set "DOWNLOAD_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"

echo download horse edition

powershell -NoProfile -Command "Invoke-WebRequest -Uri '%DOWNLOAD_URL%' -OutFile '%INSTALLER%'"

if errorlevel 1 (
    echo you failure
    pause
    exit /b 1
)

echo jimstalling
start /wait "" "%INSTALLER%" InstallAllUsers=0 PrependPath=1 Include_pip=1 Include_test=0

if errorlevel 1 (
    echo see text above 
    pause
    exit /b 1
)

set "PATH=%LocalAppData%\Programs\Python\Python315;%LocalAppData%\Programs\Python\Python315\Scripts;%PATH%"

echo.
echo checkery
python --version

echo.
echo hope
pause