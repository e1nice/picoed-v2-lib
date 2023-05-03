from picoed_v2_lib import *
from picoed_v2_lib.gy53_async import Gy53
from machine import Pin
from time import sleep_ms

gy53 = Gy53(Pin(Gpio.P15, Pin.IN))
mm = None


def gy53_handler(value):
    global mm
    mm = value


print("--- continuous - without callback ---")
gy53.callback = None
gy53.activate()
sleep_ms(100)
for x in range(6):
    if gy53.mm is None:
        print("No measurement received ({}).".format(x))
    else:
        print("mm ({}): {}".format(x, gy53.mm))
    sleep_ms(500)
gy53.deactivate()

print("--- continuous - with callback ---")
gy53.callback = gy53_handler
gy53.activate()
mm = None
sleep_ms(100)
for x in range(6):
    if mm is None:
        print("No measurement received ({}).".format(x))
    else:
        print("mm ({}): {}".format(x, mm))
    sleep_ms(500)
gy53.deactivate()

print("--- on request - without callback ---")
gy53.callback = None
for x in range(6):
    print("send request {}".format(x))
    gy53.request()
    sleep_ms(100)
    if gy53.mm is None:
        print("No measurement received ({}).".format(x))
    else:
        print("mm ({}): {}".format(x, gy53.mm))
    sleep_ms(400)

print("--- on request - with callback ---")
gy53.callback = gy53_handler
mm = None
for x in range(6):
    print("send request {}".format(x))
    gy53.request()
    sleep_ms(100)
    if mm is None:
        print("No measurement received ({}).".format(x))
    else:
        print("mm ({}): {}".format(x, mm))
    mm = None
    sleep_ms(400)
