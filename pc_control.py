# microbit-module: pc_control@0.1.0
from microbit import uart


class Keyboard():

    def write(self, text):
        uart.write("$%@s-k-txt@%${}$%@end@%$".format(text))


class Mouse():

    def move_up(self, pixels=1):
        uart.write("$%@s-m-mu@%${}$%@end@%$\n".format(pixels))

    def move_down(self, pixels=1):
        uart.write("$%@s-m-md@%${}$%@end@%$\n".format(pixels))

    def move_left(self, pixels=1):
        uart.write("$%@s-m-ml@%${}$%@end@%$\n".format(pixels))

    def move_right(self, pixels=1):
        uart.write("$%@s-m-mr@%${}$%@end@%$\n".format(pixels))

    def move_vertical(self, pixels=1):
        uart.write("$%@s-m-mv@%${}$%@end@%$\n".format(pixels))

    def move_horizontal(self, pixels=1):
        uart.write("$%@s-m-mh@%${}$%@end@%$\n".format(pixels))

    def left_click(self):
        uart.write("$%@s-m-ckl@%$$%@end@%$\n")

    def right_click(self):
        uart.write("$%@s-m-ckr@%$$%@end@%$\n")

    def scroll(self, steps=1):
        uart.write("$%@s-m-s@%${}$%@end@%$\n".format(steps))
