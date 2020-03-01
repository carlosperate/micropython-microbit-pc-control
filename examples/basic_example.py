# Basic example with Keyboard and Mouse that does left click on Button A, and
# writes "Hello, World!" on Button B.
from microbit import *

from pc_control import Keyboard, Mouse

keyboard = Keyboard()
mouse = Mouse()


def main():
    display.show(Image.HAPPY)

    while True:
        if button_a.is_pressed():
            mouse.left_click()
            sleep(500)
        if button_b.is_pressed():
            keyboard.write("Hello, World!")
            sleep(500)


if __name__ == "__main__":
    main()
