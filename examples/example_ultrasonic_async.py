from picoed_v2_lib import *
from picoed_v2_lib.ultrasonic_async import Ultrasonic
from machine import Pin
from time import sleep_ms

ultra = Ultrasonic(Pin(Gpio.P1, Pin.OUT), Pin(Gpio.P2, Pin.IN))
mm = None


def us_handler(value):
    global mm
    mm = value


print("--- continuous - without callback ---")
ultra.deactivate()
ultra.callback = None
ultra.activate()
for x in range(6):
    sleep_ms(200)
    if ultra.mm is None:
        print("No measurement received ({}).".format(x))
    else:
        print("mm ({}): {}".format(x, ultra.mm))
    sleep_ms(300)

print("--- continuous - with callback ---")
ultra.deactivate()
ultra.callback = us_handler
mm = None
ultra.activate()
for x in range(6):
    sleep_ms(200)
    if mm is None:
        print("No measurement received ({}).".format(x))
    else:
        print("mm ({}): {}".format(x, mm))
    sleep_ms(300)
ultra.deactivate()

print("--- on request - without callback ---")
ultra.deactivate()
ultra.callback = None
for x in range(6):
    ultra.request()
    sleep_ms(200)
    if ultra.mm is None:
        print("No measurement received ({}).".format(x))
    else:
        print("mm ({}): {}".format(x, ultra.mm))
    sleep_ms(300)

print("--- on request - with callback ---")
ultra.deactivate()
ultra.callback = us_handler
mm = None
for x in range(6):
    ultra.request()
    sleep_ms(200)
    if mm is None:
        print("No measurement received ({}).".format(x))
    else:
        print("mm ({}): {}".format(x, mm))
    sleep_ms(300)
