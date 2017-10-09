#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, time
sys.path.append("/home/pi/src/rtfacial/webcam/")
os.chdir("/home/pi/src/rtfacial/webcam/")
import ipget
import i2c1602a

## Get IP Address and Disp to LCD
ip = ipget.ipget()
lcd = i2c1602a.lcd(0x3f)
lcd.lcd_string(ip.ipaddr("eth0"), 1)
lcd.lcd_string("Hello world!", 2)

