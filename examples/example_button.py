from picoed_v2_lib import *
from time import sleep_ms

button_a = Button(Gpio.BUTTON_A)
button_b = Button(Gpio.BUTTON_B)

last_presses = button_a.presses
print("button_a._presses: {}".format(last_presses))
while not button_a.is_pressed() or not button_b.is_pressed():
    if button_a.presses != last_presses:
        last_presses = button_a.presses
        print("button_a._presses: {}".format(last_presses))
    if button_a.is_pressed():
        print("Button A is pressed.")
    if button_b.was_pressed():
        print("Button A has been pressed {} times.".format(button_a.reset_presses()))
    sleep_ms(200)
