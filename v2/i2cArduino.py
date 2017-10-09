import smbus
import time
import sys
#for RPI ver1, use "bus=smbus.SMBus(0)"

#This is the address we setup in the <a href="http://blog.fc2.com/tag/Arduino" class="tagword">Arduino</a> Program
class i2c:
  bus = smbus.SMBus(1)
  arduino_addr = 0x04 ## default Auduino Address
  def __init__(self, addr):
    arduino_addr = addr

  def writeNumber(self, value):
    time.sleep(0.2)
    self.bus.write_byte(self.arduino_addr, value)
    time.sleep(0.2)
    #bus.write_byte_data(address, 0, value)
 
  def get_distance(self):
    self.writeNumber(0xff)
    val = self.bus.read_byte(self.arduino_addr)
    time.sleep(0.2)
    return val
 
  def move_dc(self, i):
    ## send command 1 get angle
    ## writeNumber(1)
    ## Check return
    ## ret = readNumber()
    if (i==9):
      ## send turn 8 o'clock
      self.writeNumber(8)
    elif (i==10):
      self.writeNumber(7)
    elif (i>=11 and  i<=13):
      self.writeNumber(6)
    elif (i==14):
      self.writeNumber(5)
    elif (i==15):
      self.writeNumber(4)
    time.sleep(1)

  ##
  ## Move Survo from 9 o'clock to 15 o'clock
  ##
  def move_survo(self, i):
    ## survo 12o'clock
    self.writeNumber(i)
