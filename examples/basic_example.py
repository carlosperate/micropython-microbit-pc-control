from microbit import *

from pc_controller import Keyboard, Mouse

keyboard = Keyboard()

mouse = Mouse()


def main():
    display.show(Image.HAPPY)
    sleep(1000)

    while True:
        if buttonA.is_pressed():
            mouse.left_click()
            sleep(2000)
        if buttonB.is_pressed():
            keyboard.write("Hello, World!")
            sleep(2000)

        sleep(200)


if __name__ == "__main__":
    main()
