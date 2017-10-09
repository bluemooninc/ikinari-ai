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
    ## sudo echo $UID (sudi -i uid command)
    if (not existProc('webcam')):
      proc = subprocess.Popen('sudo -u pi -i python /home/pi/src/rtfacial/webcam/hello.py',shell=True,stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
      proc = subprocess.Popen('sudo -u pi -i python /home/pi/src/rtfacial/webcam/webcam.py',shell=True,stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)

def message(msg):
    proc = subprocess.Popen('python /home/pi/src/ikinari-ai/app/lcd.py '+msg,shell=True,stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
#
# Create functions to run when the buttons are pressed
#
def Input_2(channel):
    #GPIO.wait_for_edge(BUTTON_2, GPIO.FALLING)
    t1 = time.time()
    while True:
        sw_status = GPIO.input(BUTTON_2)
        ## It will come 0 when pushing down. After release that will be 1.
        if sw_status == 1:
            ## Time check for released push button
            if time.time() - t1 > 3:
                print("Long button")
                message("Shutdown Now!")                
                os.system("sudo shutdown -h now")
                break
            else:
                print "helo"
                hello()
                break

# Wait for Button 1 to be pressed, run the function in "callback" when it does, also software debounce for 600 ms to avoid triggering it multiple times a second
GPIO.add_event_detect(BUTTON_2, GPIO.BOTH, callback=Input_2, bouncetime=600) # Wait for Button 2 to be pressed
while True:
    sleep(1)

