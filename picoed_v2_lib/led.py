from picoed_v2_lib.gpio import Gpio
from machine import Pin


class Led:
    def __init__(self):
        self.led = Pin(Gpio.LED, Pin.OUT)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)
