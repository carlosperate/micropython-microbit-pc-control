# Simple mouse example that on Button A scrolls based on y-axes tilt.
from microbit import display, Image, accelerometer, button_a, button_b, sleep

from pc_control import Mouse

mouse = Mouse()


def main():
    display.show(Image.HAPPY)

    while True:
        if button_a.is_pressed():
            y = accelerometer.get_y()
            mouse.scroll(y // 100)
            sleep(300)


if __name__ == "__main__":
    main()
