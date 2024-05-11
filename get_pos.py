import pyautogui
from keyboard import is_pressed
import datetime
from time import sleep

pyautogui.PAUSE = 0.01

print("Tekan q untuk keluar\nTekan t untuk menyimpan")

while is_pressed("q") == False:
    sleep(0.25)
    x,y = pyautogui.position()
    print(f"x: {x}, y: {y}", end="\r")

    if (is_pressed("t")):
        f = open("./Position.txt", "a")
        current_time = datetime.datetime.now()
        f.write(f"x={x}, y={y} # {current_time} \n")
        f.close()
        print("Saving position.")
    

        