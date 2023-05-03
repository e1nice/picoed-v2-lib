from machine import Pin, time_pulse_us


class Gy53:
    def __init__(self, pin: Pin, high=True):
        self._pin = pin
        self._high = high
        self._start_tick = None
        self._us = self._mm = None

    @property
    def us(self):
        # return time_pulse_us(self._pin, 1, self.MAX_US)
        while self._pin.high():
            pass
        return time_pulse_us(self._pin, 1, 55000)

    @property
    def mm(self):
        return int(self.us * 0.1)
