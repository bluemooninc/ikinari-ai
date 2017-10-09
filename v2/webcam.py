#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys, os, time
from datetime import datetime as dt
sys.path.append("/home/pi/src/rtfacial/webcam/")
os.chdir("/home/pi/src/rtfacial/webcam/")
import cv2
import numpy as np
import face_detection_utilities as fdu
import myVGG as vgg
import ipget
# for Arduino
import i2cArduino
import i2c1602a

windowsName = 'Preview Screen'

parser = argparse.ArgumentParser(description='A live emotion recognition from webcam')
parser.add_argument('-testImage', help=('Given the path of testing image, the program will predict the result of the image.'
"This function is used to test if the model works well."))

args = parser.parse_args()
## Get IP Address and Disp to LCD
ip = ipget.ipget()
lcd = i2c1602a.lcd(0x3f)
i2c = i2cArduino.i2c(0x04)
lcd.lcd_string(ip.ipaddr("eth0"), 1)
lcd.lcd_string("Now loading data.", 2)

## Load TensorFlow Model
FACE_SHAPE = (48, 48)
emo     = ['Angry', 'Fear', 'Happy',
           'Sad', 'Surprise', 'Neutral']
model = vgg.VGG_16('my_model_weights_83.h5')

def refreshFrame(frame, faceCoordinates):
    if faceCoordinates is not None:
        fdu.drawFace(frame, faceCoordinates)
#    cv2.imshow(windowsName, frame)

def showScreenAndDectect(capture):
    i = 12
    dist = 0;
    t1 = time.time()
    while (True):
        ## 秒数上限で処理終了
        if (time.time()-t1>180):
            lcd.lcd_string("Time up!Push BTN",2)
            break
        flag, frame = capture.read()
        faceCoordinates = fdu.getFaceCoordinates(frame)
        refreshFrame(frame, faceCoordinates)
        ## 顔認識に成功した場合
        if faceCoordinates is not None:
            ## イメージを取得
            face_img = fdu.preprocess(frame, faceCoordinates, face_shape=FACE_SHAPE)
            #cv2.imshow(windowsName, face_img)
            ## save image file
            fname = "/home/pi/Pictures/face"+dt.now().strftime('%Y%m%d%H%M%S')+".jpg"
            cv2.imwrite(fname, face_img)

            input_img = np.expand_dims(face_img, axis=0)
            input_img = np.expand_dims(input_img, axis=0)
            ## TensorFlowで表情を解析する
            result = model.predict(input_img)[0]
            index = np.argmax(result)
            print (emo[index], 'prob:', max(result))
            dist = i2c.get_distance()
            lcd.lcd_string(emo[index]+':'+str(max(result)), 1)
            lcd.lcd_string(str(i)+':'+str(dist)+'cm', 2)
            ## Move except Angry
            fname = "/home/pi/Pictures/face/"+emo[index]+dt.now().strftime('%Y%m%d%H%M%S')+".jpg"
            cv2.imwrite(fname, face_img)
            if (index>=1 and index<=5):
                i2c.move_dc(i)
                if (i==9 or i==15):
                    time.sleep(0.2)
                    i2c.get_distance() 
                elif(i==11 or i==14):
                    time.sleep(0.1)
                    i2c.get_distance()

            # print(face_img.shape)
            # emotion = class_label[result_index]
            # print(emotion)
        else:
            i2c.move_survo(i)
            dist = i2c.get_distance()
            lcd.lcd_string(ip.ipaddr("eth0"), 1)
            lcd.lcd_string(str(i)+':'+str(dist)+'cm', 2)
            print ip.ipaddr("eth0") + str(i)+':'+str(dist)+'cm'
            print str(i)
            if (i<15):
                i += 1
            else:
                i = 9

def getCameraStreaming():
    capture = cv2.VideoCapture(0)
    if not capture:
        print("Failed to capture video streaming ")
        sys.exit(1)
    else:
        print("Successed to capture video streaming")
        
    return capture

def main():
    '''
    Arguments to be set:
        showCam : determine if show the camera preview screen.
    '''
    print("Enter main() function")
    
    if args.testImage is not None:
        img = cv2.imread(args.testImage)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, FACE_SHAPE)
        print(class_label[result[0]])
        sys.exit(0)

    showCam = 1
    capture = getCameraStreaming()

#    if showCam:
#        cv2.startWindowThread()
#        cv2.namedWindow(windowsName, cv2.WND_PROP_FULLSCREEN)
#        cv2.setWindowProperty(windowsName, cv2.WND_PROP_FULLSCREEN, cv2.WND_PROP_FULLSCREEN)
    
    showScreenAndDectect(capture)

if __name__ == '__main__':
    main()
