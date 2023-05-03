from machine import Pin, Timer
from time import ticks_ms, ticks_us, ticks_add, ticks_diff, sleep_us


class Ultrasonic:
    DISTANCE_FACTOR = 343 / 1000 / 2
    MAX_US = 23329

    def __init__(self, trigger_pin: Pin, echo_pin: Pin, interval_ms=200, handler=None, continuous=False):
        self._trigger_pin = trigger_pin
        self._echo_pin = echo_pin
        self._interval_ms = interval_ms
        if callable(handler):
            self._callback = handler
        else:
            self._callback = None
        self._continuous = continuous
        self._timer = Timer(-1)
        self._trigger_pin.irq(trigger=0)
        self._echo_pin.irq(trigger=0)
        self._last_req_tick_ms = ticks_add(ticks_ms(), -1 * self._interval_ms)
        self._start_tick_us = ticks_us()
        self._us = self._mm = None
        if continuous:
            self.activate()

    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, handler=None):
        if callable(handler):
            self._callback = handler
        else:
            self._callback = None

    @property
    def us(self):
        return self._us

    @property
    def mm(self):
        return self._mm

    def request(self, timer=None):
        self._last_req_tick_ms = ticks_ms()
        self._trigger_pin.low()
        sleep_us(2)
        self._trigger_pin.high()
        sleep_us(5)
        self._echo_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._cycle)
        self._trigger_pin.low()

    def _cycle(self, pin: Pin):
        # print("_cycle")
        flags = pin.irq().flags()
        if flags & Pin.IRQ_RISING:
            # print("_cycle start")
            self._start_tick_us = ticks_us()
        elif flags & Pin.IRQ_FALLING:
            # print("_cycle stop")
            stop_tick_us = ticks_us()
            self._echo_pin.irq(trigger=0)
            self._us = ticks_diff(stop_tick_us, self._start_tick_us)
            if self._us > self.MAX_US:
                self._us = -1
                self._mm = 9999
            else:
                self._mm = int(self._us * self.DISTANCE_FACTOR)
            if self._callback is not None:
                self._callback(self._mm)
            if self._continuous:
                wait_ms = max(0, self._interval_ms - ticks_diff(ticks_ms(), self._last_req_tick_ms))
                self._timer.init(period=wait_ms, mode=Timer.ONE_SHOT, callback=self.request)

    def activate(self):
        self._continuous = True
        wait_ms = max(0, self._interval_ms - ticks_diff(ticks_ms(), self._last_req_tick_ms))
        self._timer.init(period=wait_ms, mode=Timer.ONE_SHOT, callback=self.request)

    def deactivate(self):
        self._continuous = False
        self._timer.deinit()
        self._echo_pin.irq(trigger=0)
