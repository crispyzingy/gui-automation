import pyautogui

pyautogui.screenshot()
pyautogui.screenshot("example.png")
print(pyautogui.locateCenterOnScreen("calc7key.png"))
pyautogui.moveTo((934, 527), duration=1)
pyautogui.click((934, 527))
