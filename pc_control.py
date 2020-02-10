# microbit-module: pc_control@0.1.0
from microbit import uart


class Keyboard():

    def write(self, text):
        uart.write("|@s-k-txt@|{}|@e@|".format(text))


class Mouse():

    def move_up(self, pixels=1):
        uart.write("|@s-m-mu@|{}|@e@|\n".format(pixels))

    def move_down(self, pixels=1):
        uart.write("|@s-m-md@|{}|@e@|\n".format(pixels))

    def move_left(self, pixels=1):
        uart.write("|@s-m-ml@|{}|@e@|\n".format(pixels))

    def move_right(self, pixels=1):
        uart.write("|@s-m-mr@|{}|@e@|\n".format(pixels))

    def move_vertical(self, pixels=1):
        uart.write("|@s-m-mv@|{}|@e@|\n".format(pixels))

    def move_horizontal(self, pixels=1):
        uart.write("|@s-m-mh@|{}|@e@|\n".format(pixels))

    def move_relative(self, x_pixels=1, y_pixels=1):
        uart.write("|@s-m-mr@|{} {}|@e@|\n".format(x_pixels, y_pixels))

    def left_click(self):
        uart.write("|@s-m-ckl@||@e@|\n")

    def right_click(self):
        uart.write("|@s-m-ckr@||@e@|\n")

    def scroll(self, steps=1):
        uart.write("|@s-m-s@|{}|@e@|\n".format(steps))
