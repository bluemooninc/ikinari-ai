import time
import pylcdlib
import subprocess
import datetime
import sys
import os

lcd = pylcdlib.lcd(0x3f,1)

def split_str(s, n):
    "split string by its length"
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]

def to_lcd(l1,l2):
    lcd.lcd_puts(" " * 16,1)
    lcd.lcd_puts(" " * 16,2)
    lcd.lcd_puts(l1,1)
    lcd.lcd_puts(l2,2)
    lcd.lcd_backlight(1)
    print l1
    print l2


