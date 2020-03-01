# Simple mouse example that, when Button A is pressed, moves the mouse around
# based on the accelerometer data. And when Button B is pressed it performs a
# left click.
from microbit import display, Image, accelerometer, button_a, button_b, sleep

from pc_control import Mouse

mouse = Mouse()


def main():
    display.show(Image.HAPPY)

    while True:
        if button_a.is_pressed():
            x = accelerometer.get_x()
            y = accelerometer.get_y()
            mouse.move_relative(x // 10, y //10)
            sleep(50)

        if button_b.is_pressed():
            mouse.left_click()
            sleep(500)


if __name__ == "__main__":
    main()
