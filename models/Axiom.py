"""
IOT smart planter
"""
import json
import network
from models.Plant import Plant
from prephials.Lights import Halo
from prephials.Screen import Screen
from prephials.Moisture_Sensor import MoistureSensor

class Axiom:
    """ the central brain, all sensor data goes through this """
    def __init__(self):
        #read config data
        self.config = self._read_config()

        #create the access point
        self._create_access_point()

        #initialize the hardware
        self.lights =  Halo(gpio_pin=26)
        self.moisture_sensor =  MoistureSensor(gpio_pin=25)
        self.screen = Screen()

        #load the current plant from memory
        self.current_plant = self._get_current_plant()


    def _create_access_point(self): 
        """ generate access point for user to connect to """
        ap = network.WLAN(network.AP_IF)
        ap.config(essid=self.config['access_point'].name, password=self.config['access_point'].password, channel=11, authmode=2) 
        ap.config(max_clients=4) # still figuring out how i want to limit this
        ap.active(True)  

    def _read_config(self):
        """ load memory/settings from config file """
        f = open('../config.json', 'r')
        return ujson.loads(f.readall())

    def _get_current_plant(self) -> Plant:
        """ return the current plant in garden """
        for i in self.config['garden']:
            if i.current == True: return Plant(name=i.name)


    def status_report(self, current_plant):
        """ return the status report for the current plant """
        return {
            'moisture_level': self.moisture_sensor.read(),
            'plant': self.current_plant
        }

    def startup(self):
        """ launch the startup screen """
        self.screen.launch_screen()

    def go_home(self):
        """ launch the home screen """
        self.screen.home_screen()