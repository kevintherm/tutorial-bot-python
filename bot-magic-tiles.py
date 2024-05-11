import pyautogui
import time
import keyboard
import win32api, win32con

print("Automasi akan mulai dalam 3 detik!")
time.sleep(3)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN, 0, 0
    )
    time.sleep(0.01)
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTUP, 0, 0
    )

click(852, 598)
time.sleep(1)

while keyboard.is_pressed("q") == False:
    if pyautogui.pixel(682, 484)[0] == 0:
        click(682, 484) # -> Jalur 1
    
    if pyautogui.pixel(803, 464)[0] == 0:
        click(803, 464) # -> Jalur 2
    
    if pyautogui.pixel(921, 462)[0] == 0:
        click(921, 462) # -> Jalur 3
    
    if pyautogui.pixel(1042, 458)[0] == 0:
        click(1042, 458) # -> Jalur 4
    

# X:  682 Y:  484 Col 1
# X:  803 Y:  464 Col 2
# X:  921 Y:  462 Col 3
# X: 1042 Y:  458 Col 4