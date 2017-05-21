#!/usr/bin/env python2.7  
import RPi.GPIO as GPIO  
import os
import sys
import signal
import subprocess
import time
from time import sleep  # Allows us to call the sleep function to slow down our loop
import RPi.GPIO as GPIO # Allows us to call our GPIO pins and names it just GPIO

GPIO.setmode(GPIO.BCM)  # Set's GPIO pins to BCM GPIO numbering
BUTTON_2 = 21           # Sets our input pins
GPIO.setup(BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set our input pin to be an input, with internal pullup resistor on

#
# Global Value
#
menuNo = 1
pid = 0

#
# process check
#
def existProc(procName):
    ps = subprocess.Popen( 'ps aux | grep python', stdin=subprocess.PIPE,stdout=subprocess.PIPE, close_fds=True, shell=True).stdout
    for line in ps.readlines():
        if procName in line:
            print 'exist '+ procName
            return True
    print 'no exist ' + procName
    return False
#
# python process out
#
def killPythonPrg(procName='all'):
    ps = subprocess.Popen( 'ps aux | grep python', stdin=subprocess.PIPE,stdout=subprocess.PIPE, close_fds=True, shell=True).stdout
    print 'kill ' + procName
    for line in ps.readlines():
        if 'grep' or 'power' in line:
            continue
        if procName=='all' or procName in line:
            print line
            pid = line.strip().split(' ')[ 1 ]
    try:
        print 'kill -9 ' + pid
        os.killpg( os.getpgid(int(pid)), signal.SIGKILL )
    except:
        pass
#
# shutdown
#
def shutdown():
    killPythonPrg()
    print "shutdown now. Wait a green light off"
    GPIO.cleanup()          # clean up GPIO on normal exit
    os.system("/sbin/shutdown -h now")
#
# hello_world
#
def hello():
    sleep(1)
    proc = subprocess.Popen('sudo python /home/pi/ikinari-ai/lcd.py',shell=True,stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)

def message(msg):
    proc = subprocess.Popen('sudo python /home/pi/ikinari-ai/lcd.py '+msg,shell=True,stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
#
# Create functions to run when the buttons are pressed
#
def Input_2(channel):
    #GPIO.wait_for_edge(BUTTON_2, GPIO.FALLING)
    sw_counter = 0
 
    while True:
        sw_status = GPIO.input(BUTTON_2)
        if sw_status == 0:
            sw_counter = sw_counter + 1
            if sw_counter >= 100:
                print("Long button")
                message("Shutdown Now!")                
                os.system("sudo shutdown -h now")
                break
        else:
            sw_counter = 0
            print "helo"
            hello()
            break
 
        time.sleep(0.01)
 
    print(sw_counter)


# Wait for Button 1 to be pressed, run the function in "callback" when it does, also software debounce for 300 ms to avoid triggering it multiple times a second
GPIO.add_event_detect(BUTTON_2, GPIO.BOTH, callback=Input_2, bouncetime=300) # Wait for Button 2 to be pressed
while True:
    sleep(1)

