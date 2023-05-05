from machine import Pin, time_pulse_us
from time import ticks_ms, ticks_us, ticks_add, ticks_diff, sleep_us


class Ultrasonic:
    DISTANCE_FACTOR: float = 343 / 1000 / 2
    MAX_US = 23329
    INVALID_MM = 9999

    def __init__(self, trigger_pin: Pin, echo_pin: Pin, interval_ms=200):
        self._trigger_pin = trigger_pin
        self._echo_pin = echo_pin
        self._interval_ms = interval_ms
        self._last_req_tick_ms = ticks_add(ticks_ms(), -1 * self._interval_ms)
        self._start_tick_us = ticks_us()
        self._us = self._mm = None

    @property
    def us(self):
        self._trigger_pin.value(0)
        sleep_us(5)
        self._trigger_pin.value(1)
        sleep_us(10)
        self._trigger_pin.value(0)
        return time_pulse_us(self._echo_pin, 1, self.MAX_US)

    @property
    def mm(self):
        us = self.us
        if us < 0:
            return self.INVALID_MM
        else:
            return int(us * self.DISTANCE_FACTOR)
