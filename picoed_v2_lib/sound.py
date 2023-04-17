from picoed_v2_lib.gpio import Gpio
from machine import Pin, PWM
from time import sleep_ms


class Sound:
    def __init__(self):
        self.tones = {'1': 262, '2': 294, '3': 330, '4': 349, '5': 392, '6': 440, '7': 494, '-': 0}
        self.buzzer = PWM(Pin(Gpio.BUZZER))

    def play(self, melody):
        for tone in melody:
            freq = self.tones[tone]
            if freq:
                self.buzzer.duty_u16(1000)  # Adjust the frequency of the PWM to make it emit the specified tone
                self.buzzer.freq(freq)
            else:
                self.buzzer.duty_u16(0)
            # Pause (two notes per second in four-four beats, with a slight pause between notes)
            sleep_ms(400)
            self.buzzer.duty_u16(0)
            sleep_ms(100)
        self.buzzer.deinit()  # Release PWM
