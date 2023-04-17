from picoed_v2_lib.gpio import Gpio


class IIC:
    BUS0 = 0
    SDA0 = Gpio.I2C0_SDA
    SCL0 = Gpio.I2C0_SCL
    BUS1 = 1
    SDA1 = Gpio.SDA
    SCL1 = Gpio.SCL
    