"""
Example on how a micro:bit can be used to play a game that uses the arrow keys
and space bar.

When the Button A is pressed the accelerometer is used to determine which arrow
keys to press, and will keep them pressed down until the micro:bit is tilted
to a neutral position. When the Button B is pressed it presses the space bar.
"""
from microbit import display, Image, accelerometer, button_a, button_b, sleep

from pc_control import Keyboard, Mouse

keyboard = Keyboard()


def main():
    display.show(Image.HAPPY)
    up_pressed, down_pressed, left_pressed, right_pressed = False, False, False, False

    while True:
        # Only send arrow commands when Button a is pressed
        if button_a.is_pressed():
            # Hold down or release arrow keys based on accelerometer values
            x, y, z = accelerometer.get_values()
            if x > 300:
                if not right_pressed:
                    keyboard.key_down("right")
                right_pressed = True
            else:
                if right_pressed:
                    keyboard.key_up("right")
                right_pressed = False
            if x < -300:
                if not left_pressed:
                    keyboard.key_down("left")
                left_pressed = True
            else:
                if left_pressed:
                    keyboard.key_up("left")
                left_pressed = False
            if y < -300:
                if not up_pressed:
                    keyboard.key_down("up")
                up_pressed = True
            else:
                if up_pressed:
                    keyboard.key_up("up")
                up_pressed = False
            if y > 300:
                if not down_pressed:
                    keyboard.key_down("down")
                down_pressed = True
            else:
                if down_pressed:
                    keyboard.key_up("down")
                down_pressed = False

            # Display direction on matrix
            img = Image.CHESSBOARD
            if up_pressed:
                if left_pressed:
                    img = Image.ARROW_NW
                elif right_pressed:
                    img = Image.ARROW_NE
                else:
                    img = Image.ARROW_N
            elif down_pressed:
                if left_pressed:
                    img = Image.ARROW_SW
                elif right_pressed:
                    img = Image.ARROW_SE
                else:
                    img = Image.ARROW_S
            elif left_pressed:
                img = Image.ARROW_W
            elif right_pressed:
                img = Image.ARROW_E
            display.show(img, delay=50, wait=False)
        else:
            if up_pressed:
                keyboard.key_up("up")
            if down_pressed:
                keyboard.key_up("down")
            if left_pressed:
                keyboard.key_up("left")
            if right_pressed:
                keyboard.key_up("right")
            up_pressed, down_pressed, left_pressed, right_pressed = False, False, False, False
            display.show(Image.HAPPY)

        # Press keys when buttons are pressed
        if button_b.is_pressed():
            keyboard.press("space")
            display.show("S")
            sleep(150)


if __name__ == "__main__":
    main()
