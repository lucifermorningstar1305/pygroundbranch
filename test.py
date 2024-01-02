
from keyboard_mouse_events import main
from pynput import keyboard

if __name__ == "__main__":
    
    while True:
        ret = main()
        if ret == keyboard.Key.f10:
            print("DONE!")
            break
