from machine import Pin
from time import ticks_us, ticks_diff


class Gy53:
    def __init__(self, pin, handler=None, high=True, continuous=False):
        self._pin = pin
        self._high = high
        self._continuous = continuous
        if callable(handler):
            self._callback = handler
        else:
            self._callback = None
        if self._high:
            self._start_irq = Pin.IRQ_RISING
            self._stop_irq = Pin.IRQ_FALLING
        else:
            self._start_irq = Pin.IRQ_FALLING
            self._stop_irq = Pin.IRQ_RISING
        self._pin.irq(trigger=0)
        self._start_tick = None
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

    def request(self):
        # print("request")
        self._pin.irq(trigger=0)
        self._us = self._mm = None
        self._pin.irq(trigger=self._stop_irq, handler=self._end_cycle)

    def _end_cycle(self, pin: Pin):
        # print("_end_cycle")
        pin.irq(trigger=self._start_irq | self._stop_irq, handler=self._cycle)

    def _cycle(self, pin: Pin):
        # print("_cycle")
        flags = pin.irq().flags()
        if flags & self._start_irq:
            # print("_cycle start")
            self._start_tick = ticks_us()
        elif flags & self._stop_irq:
            # print("_cycle stop")
            stop_tick = ticks_us()
            if not self._continuous:
                self._pin.irq(trigger=0)
            self._us = ticks_diff(stop_tick, self._start_tick)
            self._mm = int(self._us * 0.1)
            if self._callback is not None:
                self._callback(self._mm)

    def activate(self):
        # print("activate")
        self._pin.irq(trigger=0)
        self._continuous = True
        self._pin.irq(trigger=self._stop_irq, handler=self._end_cycle)

    def deactivate(self):
        # print("deactivate")
        self._pin.irq(trigger=0)
        self._continuous = False
