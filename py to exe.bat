@ECHO OFF
cls
title PY to EXE
color 4a
del launcher.exe
del CSGO-Gratuit.exe
echo INIT 1/2
pyinstaller --onefile --windowed launcher.py
echo INIT 2/2
pyinstaller --onefile CSGO-Gratuit.py
rmdir /S /Q build
rmdir /S /Q __pycache__
del CSGO-Gratuit.spec
del launcher.spec
move dist\CSGO-Gratuit.exe
move dist\launcher.exe
rmdir /Q dist