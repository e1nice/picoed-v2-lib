from .is31fl3731 import Matrix
from .gpio import Gpio
from .iic import IIC
from .image import Image
from .display import Display
from machine import I2C, Pin
from .led import Led
from .button import Button
from .music import Music


i2c0 = I2C(IIC.BUS0, scl=Pin(IIC.SCL0), sda=Pin(IIC.SDA0))
display = Display(i2c0)
led = Led()
button_a = Button(Gpio.BUTTON_A)
button_b = Button(Gpio.BUTTON_B)
music = Music(Pin(Gpio.BUZZER))
