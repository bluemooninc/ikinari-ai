#!/bin/bash
## capture
cd /home/pi/ikinari-ai
sudo /home/pi/.anyenv/envs/pyenv/shims/python lcd.py Start-WebCam
sudo /usr/bin/fswebcam /home/pi/ikinari-ai/tmp.jpg

## Resize and CNN
sudo /home/pi/.anyenv/envs/pyenv/shims/python lcd.py Resize-Image.
/home/pi/.anyenv/envs/pyenv/shims/python moveresize.py
sudo /home/pi/.anyenv/envs/pyenv/shims/python lcd.py TensorFlow-Now
/home/pi/.anyenv/envs/pyenv/shims/python xception.py

## Speak to TensorFlow responce
sudo /home/pi/.anyenv/envs/pyenv/shims/python lcd.py
/home/pi/.anyenv/envs/pyenv/shims/python espeak.py

## Send GO command to Arduino
/home/pi/.anyenv/envs/pyenv/shims/python i2c.py

