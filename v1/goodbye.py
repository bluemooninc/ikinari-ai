import time
import pylcdlib
import subprocess
import datetime
import sys
import glob
import os

lcd = pylcdlib.lcd(0x3f,1)

def show_ip():
  title = "Shutdown Now!"
  dt = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
  lcd.lcd_puts(" " * 16,1)
  lcd.lcd_puts(" " * 16,2)
  lcd.lcd_puts(dt,1) #line1
  lcd.lcd_puts(title,2) #line2
  time.sleep(3)

show_ip()

