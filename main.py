from colored import fg, attr, bg
import os, time, pyautogui, threading, keyboard, sys, ctypes

os.system("@echo off")
os.system("title Password")
os.system("cls")

response = "azerty"

pyautogui.press("F11")

def F11_spam():
    c = True
    while True:
        if keyboard.is_pressed("F11") and c:
            c = False
            pyautogui.press("F11")
            os.system("color 40")
            time.sleep(0.1)
            c = True
        if keyboard.is_pressed("q"):
            os.system("exit")
        

def Main():
    while True: 
        os.system("color 40")
        os.system("cls")
        user_response = input(f"{fg(0)}{bg(1)}Entrez votre clé ici: \n{attr(0)}")


        if user_response == response:
            print(f"{fg(2)}{bg(1)}Clé valide{attr(0)}")
            print(f"{fg(0)}{bg(1)}Appuyez sur une touche pour quitter{attr(0)}")
            os.system("pause >nul")
            break
        else:
            print(f"{fg(88)}{bg(1)}Clé invalide{attr(0)}")
            time.sleep(0.5)


main = threading.Thread(target=Main)
f11_spam = threading.Thread(target=F11_spam)

threads = [main, f11_spam]

for thread in threads:
    thread.start()


for thread in threads:
    thread.join()
