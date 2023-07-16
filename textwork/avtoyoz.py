import pyautogui
import time

time.sleep(4)
c = 1
while c < 50:
    pyautogui.typewrite("Salom      O'g'iloy ")
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.typewrite("Nimagaplar olamdaa ?")
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'b')
    pyautogui.hotkey('ctrl', 'i')
    pyautogui.hotkey('ctrl', 'shift', 'P')
    pyautogui.press("enter")
    c += 1
# pyautogui.alert('This displays some text with an OK button.')
# # pyautogui.confirm('This displays text and has an OK and Cancel button.')
#
# pyautogui.prompt('This lets the user type in a string and press OK.')
