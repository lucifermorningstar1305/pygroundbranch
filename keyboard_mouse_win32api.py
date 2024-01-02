import win32api as wapi
import time


def get_mouse_pos():
    return wapi.GetCursorPos()

def get_mouse_click():
    special_keys = {
        0x01: "leftClick",
        0x02: "rightClick",
        0x04: "middleClick"
    }

    for i in range(1, 256):
        if wapi.GetAsyncKeyState(i):
            if i in special_keys:
                return special_keys[i]
            