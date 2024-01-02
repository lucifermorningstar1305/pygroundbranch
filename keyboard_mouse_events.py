"""
Citation: https://discuss.python.org/t/running-keyboard-and-mouse-listener-at-the-same-time/13416/4

"""

from pynput import keyboard, mouse
from collections import defaultdict
import time
import math
import gc


def on_move(x, y):
    pass


def on_press(key):
    print(f"Key pressed: {key}")


def on_release(key):
    pass


def onclick(x, y, button, pressed):
    if pressed:
        print(button)


def onscroll(x, y, dx, dy):
    try:
        print(dy)
    except Exception as exc:
        pass


def checkMouseEvent():
    with mouse.Events() as mevents:
        mevent = mevents.get(0.1)

        if mevent is not None:
            if "Move" in str(mevent):
                return on_move(mevent.x, mevent.y)

            if "Click" in str(mevent):
                return onclick(mevent.x, mevent.y, mevent.button, mevent.pressed)

            if "Scroll" in str(mevent):
                return onscroll(mevent.x, mevent.y, mevent.dx, mevent.dy)


def checkKeyboardEvent():
    with keyboard.Events() as kevents:
        kevent = kevents.get(0.1)

        if kevent is not None:
            if "Press" in str(kevent):
                on_press(kevent.key)


if __name__ == "__main__":
    while True:
        ret = checkMouseEvent()
        checkKeyboardEvent()
        if ret is not None:
            deltaX = 990 - ret[0]
            deltaY = 540 - ret[1]

            print(math.degrees(math.atan2(deltaY, deltaX)))


# import pyautogui

# if __name__ == "__main__":
#     try:
#         while True:
#             x, y = pyautogui.position()
#             print(x, y)
#     except Exception as e:
#         print(e)
