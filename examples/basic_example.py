from microbit import *

from pc_control import Keyboard, Mouse

keyboard = Keyboard()
mouse = Mouse()


def main():
    display.show(Image.HAPPY)
    sleep(1000)

    while True:
        if button_a.is_pressed():
            mouse.left_click()
            sleep(500)
        if button_b.is_pressed():
            keyboard.write("Hello, World!")
            sleep(500)


if __name__ == "__main__":
    main()
