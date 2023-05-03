from picoed_v2_lib import *
from time import sleep_ms

led = Led()
for x in range(6):
    led.on()
    sleep_ms(500)
    led.off()
    sleep_ms(500)
