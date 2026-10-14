@echo off
title pithen
echo ================
echo pete install
echo please run this twice so PATH registers
echo thank you
echo ================
echo working...
powershell -Command "powershell -ExecutionPolicy ByPass -c 'irm https://astral.sh/uv/install.ps1 | iex'"

powershell -Command "uv python install"
for /f "delims=" %%P in ('uv python find 3.15') do set "PYTHON_EXE=%%P"
for %%P in ("%PYTHON_EXE%") do set "PYTHON_DIR=%%~dpP"

powershell -NoProfile -ExecutionPolicy Bypass -Command "$dir = $env:PYTHON_DIR.TrimEnd('\'); $p = [Environment]::GetEnvironmentVariable('Path', 'User'); $entries = @($p -split ';' | Where-Object { $_ }); if ($entries -notcontains $dir) { [Environment]::SetEnvironmentVariable('Path', (($entries + $dir) -join ';'), 'User') }"

set "PATH=%PYTHON_DIR%;%PATH%"
python --version
echo hope
pause