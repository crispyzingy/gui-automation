# draws a square spiral shape
# open paint or any such drawing app and place mouse over it and then run this python program

import pyautogui

pyautogui.click()  # click to put drawing program in focus
distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0.1)  # move right
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.1)  # move down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.1)  # move left
    distance = distance - 25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=0.1)  # move up

