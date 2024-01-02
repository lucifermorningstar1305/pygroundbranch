from typing import Tuple, List, Dict, Any 
from pynput import keyboard, mouse

from collections import defaultdict

def on_move(x, y) -> Tuple:
    ACTIONS["mouse"].append((x, y))


def on_press(key) -> str:
   ACTIONS["keyboard"].append(key)


def on_release(key):

    if key == keyboard.Key.esc:
        mlistener.stop()
        klistener.stop()
        return False
    


def on_click(x, y, button, pressed) -> str:
    if pressed:
       if button == mouse.Button.left:
           ACTIONS["mouse"].append("left")
       
       elif button == mouse.Button.right:
          ACTIONS["mouse"].append("right")
       
       elif button == mouse.Button.middle:
           ACTIONS["mouse"].append("middle")
       
       else:
           return ""


def on_scroll(x, y, dx, dy) -> str:
    try:
        if dy > 0:
           ACTIONS["mouse"].append("scroll_up")
        else:
            ACTIONS["mouse"].append("scroll_down")
    except Exception as exc:
        pass

if __name__ == "__main__":
    ACTIONS = defaultdict(lambda: list())

    with keyboard.Listener(on_press=on_press, on_release=on_release) as klistener, mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mlistener:
        
        klistener.join()
        mlistener.join()

        print(klistener, mlistener)

    print(ACTIONS)