from machine import Pin
from time import sleep_ms


class Button:
    def __init__(self, gpio_nr):
        self._button = Pin(gpio_nr, Pin.IN, Pin.PULL_UP)
        self._presses = 0
        self._flags = None
        self._is_pressed = False
        self._button.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.callback)

    def callback(self, pin: Pin):
        flags = pin.irq().flags()
        self._flags = flags
        if flags & Pin.IRQ_FALLING:
            self._is_pressed = True
            self._presses += 1
        else:
            self._is_pressed = False

    def is_pressed(self):
        return self._is_pressed

    def presses(self):
        presses = self._presses
        self._presses = 0
        return presses

    def was_pressed(self):
        presses = self._presses
        self._presses = 0
        return presses > 0
