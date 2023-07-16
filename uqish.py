import pyautogui
import time

time.sleep(4)
c = 1
while c < 100:
    pyautogui.typewrite(
        "mandayam savol bor, maqsad bo'lmasa nima qilish kerak. Maqsad ham yo'qolib qolgan vaqti, qanday qilib yangi maqsad qo'yish kerak ?")
    pyautogui.press("enter")
    c += 1
