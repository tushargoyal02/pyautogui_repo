# SOME COMMAN COMMAND FOR FUTURE

import pyautogui


# move the cursor left right up to the point according to  current location
''' - up and bottom (-x mean to the left, -y mean to the up)

# Click mouse button
-> pyautogui.rightClick()
-> pyautogui.doubleClick()

-> pyautogui.click(button='right', click=2, interval=0.1)
      - denote the type of click, number of time click and interval of click

# Drag and drop of mouse
-> pyautogui.moveTo(x,y,duartion=1)
-> pyautogui.mouseDown(button='left')
-> pyautogui.moveTo(x2,y2, duration=2)
-> pyautogui.mouseUp(button='left')
  
  OR
->  pyautogui.moveTo(x2,y2, duration=2)
->  pyautogui.dragTo(x2,y2, duration=2)


'''
pyautogui.move(380,115)





