import pyautogui
import keyboard
import time

print("Automasi akan mulai dalam 3 detik!")
time.sleep(3)

while keyboard.is_pressed("q") == False:
    pyautogui.click(623, 774) # -> Ubah ke kordinat sesuai posisi di window
    time.sleep(0.1)

    pyautogui.typewrite("Hello World!!")
    pyautogui.press("enter")
