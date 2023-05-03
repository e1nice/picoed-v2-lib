from picoed_v2_lib import *
from machine import I2C, Pin

i2c0 = I2C(IIC.BUS0, scl=Pin(IIC.SCL0), sda=Pin(IIC.SDA0))
i2c1 = I2C(IIC.BUS1, scl=Pin(IIC.SCL1), sda=Pin(IIC.SDA1), freq=100000)

for bus_id in range(2):
    if bus_id == 0:
        bus = i2c0
    else:
        bus = i2c1
    devices = bus.scan()
    if len(devices) == 0:
        print("No devices found on bus {}.".format(bus_id))
    else:
        print("Devices found on bus {}:".format(bus_id))
        for device in devices:
            print("  Address: ", hex(device))
    