import win32api
import win32con

ms = 0
ms_max = int(input("Set click speed : "))


def mouse_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, win32api.GetCursorPos()[0], win32api.GetCursorPos()[1])


while True:
    ms += 1
    if ms == ms_max * 180:
        mouse_click()
        ms = 0
