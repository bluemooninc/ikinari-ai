import smbus2
import time
#for RPI ver1, use "bus=smbus.SMBus(0)"
bus=smbus2.SMBus(1)

# timeout variable can be omitted, if you use specific value in the while condition
timeout = 30   # [seconds]
timeout_start = time.time()

#This is the address we setup in the <a href="http://blog.fc2.com/tag/Arduino" class="tagword">Arduino</a> Program
address = 0x04
 
def writeNumber(value):
        bus.write_byte(address, value)
        #bus.write_byte_data(address, 0, value)
        return -1
 
def readNumber():
	number = bus.read_byte(address)
	# number = bus.read_byte_data(address, 1)
	return number
 
def main():
    while time.time() < timeout_start + timeout:
        ## send command 1 as GO GO GO!
        writeNumber(1)
        #sleep one second
        time.sleep(1)
        ## Check return
        number=readNumber()
        if (number == 1):
            print "Go "
    ## Stop when time out
    writeNumber(2)
    time.sleep(1)
    number=readNumber()
    if (number == 2):
        print "Stop "
 
if __name__ == '__main__':
        main() #! /usr/bin/env /usr/bin/python
 
