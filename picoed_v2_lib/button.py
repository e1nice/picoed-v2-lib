from machine import Pin, Timer


class Button:
    def __init__(self, gpio_nr, pressed_value=False):
        self._pin = Pin(gpio_nr, Pin.IN, Pin.PULL_UP)
        self._pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self._irq_handler)
        self._pressed_value = pressed_value
        self._DEBOUNCE_MS = 20
        self._presses = 0
        self.db_timer = Timer(-1)

    def _irq_handler(self, pin: Pin):
        self.db_timer.init(mode=Timer.ONE_SHOT, period=self._DEBOUNCE_MS, callback=self._debounce_handler)
        self._pin.irq(trigger=0)

    def _debounce_handler(self, t: Timer):
        if self._pin.value() == self._pressed_value:
            self._presses += 1
        self._pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self._irq_handler)

    @property
    def presses(self):
        return self._presses

    def is_pressed(self):
        return self._pin.value() == self._pressed_value

    def reset_presses(self):
        presses = self._presses
        self._presses = 0
        return presses

    def was_pressed(self):
        if self._presses == 0:
            return 0
        else:
            presses = self._presses
            self._presses = 0
            return presses
