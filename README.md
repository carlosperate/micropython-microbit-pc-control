# MicroPython micro:bit PC Control module

A MicroPython library for the BBC micro:bit that enables control of the
keyboard and mouse from the connected computer.

The [Serial PC Control][1] app needs to be running on the PC for this library
to function.


A sample of the Mouse API:

```python
from pc_control import Mouse

mouse = Mouse()

mouse.left_click()
mouse.right_click()
mouse.move_relative(x_pixels=10,  y_pixels=10)
```

A sample of the Keyboard API:

```python
from pc_control import Keyboard

keyboard = Keyboard()

keyboard.write("Hello, World!")
keyboard.press("enter")
```

Have a look at the [examples](examples) folder to see more examples, and the
[libray source code](pc_control.py) to see all the available methods.

[1]: https://github.com/carlosperate/python-serial-pc-control
