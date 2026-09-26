@echo off
cd ..
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/bebeday10/penguin-3/archive/refs/heads/main.zip' -OutFile 'penguin3.zip'"
powershell -Command "Expand-Archive -Path 'penguin3.zip' -DestinationPath '.' -Force"
del penguin3.zip
pip install -U penglang
