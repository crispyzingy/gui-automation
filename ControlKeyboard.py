import pyautogui

pyautogui.click()  # to bring the typing program to focus

# comment out what's not used
pyautogui.typewrite("Hello world!", interval=0.1)
# pyautogui.typewrite(
#     ["a", "b", "left", "left", "X", "Y"], interval=1
# )  # presses the buttons
# pyautogui.press("F1")  # press a keyboard shortcut
# pyautogui.hotkey("ctrl", "o")  # for pressing combinations of hotkeys
