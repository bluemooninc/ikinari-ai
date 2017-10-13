#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import smbus
import time

I2C_ADDRESS = 0x04    ## Arduino Slave Device ADDRESS
bus = smbus.SMBus(1)  ## Use Raspberry Pi SMBus
WAIT_TIME = 0.2       ## Time to sleep between the signale

def loop():
    ## Send Byte Data as a command
    bus.write_byte(I2C_ADDRESS, 0xff)
    ## Time constant
    time.sleep(WAIT_TIME)
    ## Send Request for get data from Arduino
    value=bus.read_byte(I2C_ADDRESS)
    print "Return: "+str(value)
    ## send DC on
    time.sleep(WAIT_TIME)
    bus.write_byte(I2C_ADDRESS, 253)
    time.sleep(1)

    t=threading.Timer(WAIT_TIME, loop)
    t.start()

t=threading.Thread(target=loop)
t.start()
