@ECHO OFF
cls
title PY to EXE
color 4a
echo INIT 1/4
pyinstaller --onefile password.py
echo INIT 2/4
pyinstaller --onefile --windowed CSGO-GRATUIT.py
echo INIT 3/4
pyinstaller --onefile --windowed c.py
echo INIT 4/4
pyinstaller --onefile relaunch.py
rmdir /S /Q build
rmdir /S /Q __pycache__
del CSGO-GRATUIT.spec
del c.spec
del relaunch.spec
del password.spec