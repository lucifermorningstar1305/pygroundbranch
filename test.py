
# from keyboard_mouse_events import main
# from pynput import keyboard

from keyboard_mouse_win32api import get_mouse_pos, get_mouse_click
if __name__ == "__main__":
    
    while True:

        print(get_mouse_pos())
        print(get_mouse_click())
        # ret = main()
        # if ret == keyboard.Key.f10:
        #     print("DONE!")
        #     break
