#importing library
import pyautogui, time

# It return the location of mouse
# value are Point(x=333, y=74)
print(pyautogui.position())

# clicking on the browser
time.sleep(5)
pyautogui.click(333, 74)
pyautogui.typewrite("https://instagram.com")

# square bracket denotes it is the keyboard command
pyautogui.typewrite(["Enter"])


# hotkeys are used to combine many keys
# --- pyautogui.hotkey("ctrl","c")

# 704,139
time.sleep(5)
pyautogui.click(704, 139)
time.sleep(2)
pyautogui.typewrite("deepikapadukone")
time.sleep(3)
#pyautogui.typewrite(["Enter"])

# Celebrity click
pyautogui.click(725, 209)
time.sleep(3)

# followers click Point(x=738, y=302)
pyautogui.click(738, 302)
time.sleep(3)

# to make follow Point(x=861, y=298)
pyautogui.click(861, 298)
time.sleep(4)
pyautogui.scroll(-7)

print("hello")

''' some other command
- pyautogui.moveTo(x,y, duration= 2)   //duartion is after how much second

'''
#CGI