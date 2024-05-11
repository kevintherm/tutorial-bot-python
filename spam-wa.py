import pyautogui
import keyboard
import time

print("Automasi akan mulai dalam 3 detik!")
time.sleep(3)

while keyboard.is_pressed("q") == False:
    pyautogui.click(x=316, y=867) # -> Ubah ke kordinat sesuai posisi di window
    time.sleep(0.1)

    pyautogui.typewrite("Hello World!!")
    pyautogui.press("enter")
