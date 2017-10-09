#!/bin/bash
## capture
/home/pi/.anyenv/envs/pyenv/shims/python espeak.py "Take a picture now!"
cd /home/pi/ikinari-ai
sudo /home/pi/.anyenv/envs/pyenv/shims/python lcd.py Run TensorFlow
sudo /usr/bin/fswebcam /home/pi/ikinari-ai/tmp.jpg

## Resize and CNN
sudo /home/pi/.anyenv/envs/pyenv/shims/python lcd.py
/home/pi/.anyenv/envs/pyenv/shims/python moveresize.py
/home/pi/.anyenv/envs/pyenv/shims/python xception.py

## Speak to TensorFlow responce
/home/pi/.anyenv/envs/pyenv/shims/python espeak.py "My answer is"
/home/pi/.anyenv/envs/pyenv/shims/python espeak.py

## Send GO command to Arduino
/home/pi/.anyenv/envs/pyenv/shims/python i2c.py

