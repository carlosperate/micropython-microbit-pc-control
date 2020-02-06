# microbit-module: pc_control@0.1.0
from microbit import uart


class Keyboard():

    def write(self, text):
        uart.write("$%@k-txt@%${}".format(text))


class Mouse():

    def left_click():
        uart.write("$%@m-ckl@%$")

    def right_click():
        uart.write("$%@m-ckr@%$")
