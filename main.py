import pyautogui
import time
import keyboard
import win32api, win32con
import webbrowser as wb

def ButtonPress(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

wb.open("https://www.crazygames.pl/gra/magic-piano-tiles")
time.sleep(3)
ButtonPress(1007, 325) #close add
time.sleep(6)
ButtonPress(770, 550) #second add
time.sleep(2)
ButtonPress(770, 500) #start button

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(630, 550)[0] == 0:
        ButtonPress(630, 550)
    if pyautogui.pixel(720, 550)[0] == 0:
        ButtonPress(720, 550)
    if pyautogui.pixel(810, 550)[0] == 0:
        ButtonPress(810, 550)
    if pyautogui.pixel(900, 550)[0] == 0:
        ButtonPress(900, 550)
