import pyautogui
import keyboard
import time

#print(pyautogui.position())
"""
pyautogui.moveTo(1246, 1175, duration=1)
pyautogui.click()
pyautogui.write("ahoj", interval=1)
"""
while True:
    if keyboard.is_pressed("a"):
        break
    time.sleep(0.1)
    pyautogui.click()