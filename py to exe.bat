@ECHO OFF
cls
title PY to EXE
color 4a
del launcher.exe
del main.exe
echo INIT 1/2
pyinstaller --onefile --windowed launcher.py
echo INIT 2/2
pyinstaller --onefile main.py
rmdir /S /Q build
rmdir /S /Q __pycache__
del main.spec
del launcher.spec
move dist\main.exe
move dist\launcher.exe
rmdir /Q dist