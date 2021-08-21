from machine import Pin, ADC

class MoistureSensor:
    """ measures the amount of water in the soil """
    def __init__(self, gpio_pin: int):
        self.__sensor = ADC(Pin(gpio_pin))
        self.__sensor.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
        self.__sensor.width(ADC.WIDTH_9BIT)   # set 9 bit return values (returned range 0-511)
    
    def read(self) -> int:
        """ read the ouput from sensor """
        return self.__sensor.read()
    
    def get_percentage(self) -> float:
        """ convert sensor data to percentage """
        return (self.read() / 511) * 100