from picoed_v2_lib import *
from time import sleep
from machine import I2C, Pin

i2c0 = I2C(IIC.BUS0, scl=Pin(IIC.SCL0), sda=Pin(IIC.SDA0))
display = Display(i2c0)

display.show(1234567890)
display.scroll("abcdefghijklmnopqrstuvwxyz")
display.show(Image.HAPPY, 20)
sleep(4)
display.clear()
