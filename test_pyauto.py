import pyautogui
import keyboard

pyautogui.click(861, 298)
x=0
while x<=1000:
    pyautogui.scroll(-1)
    pyautogui.click(861, 298, duration=0.6)
    #print(pyautogui.getWindows())
    pyautogui.FAILSAFE = True
    if keyboard.is_pressed('q'): 
        break
    x=x+1



 