from picoed_v2_lib import *
from picoed_v2_lib.ultrasonic import Ultrasonic
from machine import Pin
from time import sleep_ms

ultra = Ultrasonic(Pin(Gpio.P1, Pin.OUT), Pin(Gpio.P2, Pin.IN))

for x in range(20):
    sleep_ms(200)
    print("ultra.mm: {}".format(ultra.mm))
    sleep_ms(300)
