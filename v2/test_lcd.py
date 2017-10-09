#import lcd
import ipget

ip = ipget.ipget()
print ip.ipaddr("eth0")
#lcd.to_lcd(ip,'')

import i2c1602a
lcd = i2c1602a.lcd(0x3f)
lcd.lcd_string("Hello",1) #display "Raspberry Pi" on line 1
lcd.lcd_string("World!",2) #display "Take a byte!" on line 2
