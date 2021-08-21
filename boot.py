try:
  import usocket as socket
except:
  import socket

from models.Axiom import Axiom

import esp
esp.osdebug(None)

import gc
gc.collect()

#initialze the axiom 
axiom = Axiom()

#if awaken from deep sleep show launch screen
axiom.startup()

# initialize the screen
spi = machine.SPI(1, baudrate=32000000)

#create axios object and load garden data into memory

