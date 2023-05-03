from picoed_v2_lib import *
from picoed_v2_lib.gy53 import Gy53
from machine import Pin
from time import sleep_ms

gy53 = Gy53(Pin(Gpio.P15, Pin.IN))

for x in range(20):
    sleep_ms(200)
    print("gy53.mm: {}".format(gy53.mm))
    sleep_ms(300)
