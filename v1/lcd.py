import time
import pylcdlib
import subprocess
import datetime
import sys
import glob
import os

argvs = sys.argv
argc = len(argvs)

lcd = pylcdlib.lcd(0x3f,1)

dirname = '/home/pi/ikinari-ai/static/img/*.jpg.txt'
img_path = max(glob.iglob(dirname), key=os.path.getctime)


def split_str(s, n):
    "split string by its length"
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]

def to_lcd(l1,l2):
    lcd.lcd_puts(" " * 16,1)
    lcd.lcd_puts(" " * 16,2)
    lcd.lcd_puts(l1,1)
    lcd.lcd_puts(l2,2)
    print l1
    print l2

def load_text():
  f = open(img_path)
  str = f.read()
  arr = split_str(str, 32)
  f.close
  line1=arr[0][0:15]
  line2=arr[0][16:31]
  to_lcd(line1,line2)
  time.sleep(3)

def show_ip():
  cmd = 'ifconfig | grep inet | grep -v "127" | cut --delimiter ":" -f 2 | sed -e "s/ .*//"'
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout_data, stderr_data = p.communicate()
  ip = stdout_data.rstrip()
  dt = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
  to_lcd(dt,ip)
  time.sleep(3)


if (argc == 2):
  lcd.lcd_puts(" " * 16,1)
  lcd.lcd_puts(" " * 16,2)
  lcd.lcd_puts(argvs[1],1)
else:
  lcd.lcd_puts(" " * 16,1)
  lcd.lcd_puts(" " * 16,2)
  load_text()
  lcd.lcd_puts(" " * 16,1)
  lcd.lcd_puts(" " * 16,2)
  show_ip()

##lcd.lcd_clear()

