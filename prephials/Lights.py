from machine import Pin, PWM

class Halo: 
    """ class to manage the grow lights """
    def __init__(self, gpio_pin: int):
        self.__lights = Pin(gpio_pin, Pin.OUT)
        self.__lvl = PWM(self.__lights)

    def turn_on(self):
        """ turn on the lights """
        self._lights.value(0)

    def turn_off(self):
        """ turn off the lights """
        self._lights.value(1)

    def adjust_brightness(self, percentage):
        """ adjust the brightness of lights """
        self__lvl.duty(int(percentage * 1023 / 100));
