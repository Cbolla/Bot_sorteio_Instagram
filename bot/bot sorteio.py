import pyautogui
import time

while True:
    if pyautogui.locateOnScreen("esperar.PNG"):
        time.sleep(15)
    if pyautogui.locateOnScreen("chat.PNG"):
        pyautogui.click("chat.PNG")
        time.sleep(1)
        pyautogui.write("vou ganhar")
        time.sleep(10)
    if pyautogui.locateOnScreen("post.PNG"):
        pyautogui.locateOnScreen("post.PNG")
        pyautogui.click("post.PNG")
        time.sleep(3)
    