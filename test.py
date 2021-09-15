import pyautogui, keyboard, time

screenWidth, screenHeight = pyautogui.size()
pyautogui.FAILSAFE = False

while True:
    
    keyboard.wait("ctrl+alt+suppr")
    print('click')
    time.sleep(1.5)
    pyautogui.press("escape")
    print("ok")
