"""
Citation: https://stackoverflow.com/questions/45973453/using-mouse-and-keyboard-listeners-together-in-python
"""


from typing import Tuple, List, Dict, Any 

import mouse as pym
import keyboard as pyk
from pynput import keyboard, mouse

from collections import defaultdict

ACTIONS = defaultdict(lambda: list())
KLISTENER = None
MLISTINER = None

def on_move(x, y) -> Tuple:
    ACTIONS["mouse_movement"].append((x, y))


def on_press(key) -> str:
   ACTIONS["keyboard"].append(key)


def on_release(key):
    if key == keyboard.Key.f10:
        KLISTENER.stop()
        MLISTINER.stop()
        return False
    


def on_click(x, y, button, pressed) -> str:
    if pressed:
       if button == mouse.Button.left:
           ACTIONS["mouse_click"].append("left")
       
       elif button == mouse.Button.right:
          ACTIONS["mouse_click"].append("right")
       
       elif button == mouse.Button.middle:
           ACTIONS["mouse_click"].append("middle")
       
       else:
           return ""


def on_scroll(x, y, dx, dy) -> str:
    try:
        if dy > 0:
           ACTIONS["mouse_scroll"].append("scroll_up")
        else:
            ACTIONS["mouse_scroll"].append("scroll_down")
    except Exception as exc:
        pass

def main():
    global KLISTENER
    global MLISTINER
    
    pyk.wait("0")
    print("START!!")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as klistener, mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mlistener:
        
        KLISTENER = klistener
        MLISTINER = mlistener

        klistener.join()
        mlistener.join()

    print(ACTIONS)

    return ACTIONS["keyboard"][-1]