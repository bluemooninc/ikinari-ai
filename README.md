# Demo
[Video](https://www.facebook.com/bluemooncorp/videos/1457639287613836/)

![img_20171010_084322](https://user-images.githubusercontent.com/1677443/31363247-161076e8-ad98-11e7-838e-0da55427315a.jpg)

日本語の解説はこちら＞(https://github.com/bluemooninc/ikinari-ai/wiki)

リアルタイム・動体検知撮影ができるカメラを搭載し、スマホによる遠隔操作が可能で動体検知時に様々なアクションを起こす事ができるAiロボットです。

TensorFlow を中心に Keras フレームワークを使用して、IoTデバイスを制御する仕組みを研究する為のロボットです。ハードウェアは Raspberry Pi / Arduino を中心に シリアル通信デバイス、DCモーター、サーボモーターを制御できます。サンプルプログラムでは、人の顔の表情を解析して追いかけます。

# Raspberry Pi / AI Robot project

This project using Raspberry and Arduino Ai robot project.
We can learn about how to build a robot with open sources.

```
 1:How to connect Raspberry Pi and Arduino whitch using I2C protcol.
 2:How to connect 1602A serial LCD from Raspberry Pi.
 3:How to control Single DC motor with TIP120 transistor and Power.
 4:How to control Dual DC motor with L298 Motor Driver Module.
 5:How to control SG90 Survo motor.
 6:How to connect HC-SR04 Ultrasonic Sensor.
 7:How to connect USB WebCam and realtime capture from Raspberry Pi.
 8:How to processing real time face segmentation using Keras, TensorFlow and OpenCV2.
```

# 1:You may need modules install

    pip install numpy
    pip install cython
    pip install scipy
    pip install h5py
    pip install pillow
    pip install keras

# 2:After that you need install tenforflow

    https://github.com/samjabrahams/tensorflow-on-raspberry-pi
 
# 3:make sure Versions

    >pip list
    click (6.7)
    Cython (0.25.2)
    Flask (0.12.1)
    funcsigs (1.0.2)
    h5py (2.7.0)
    itsdangerous (0.24)
    Jinja2 (2.9.6)
    Keras (2.0.4)
    MarkupSafe (1.0)
    mock (2.0.0)
    numpy (1.12.1)
    olefile (0.44)
    pbr (3.0.0)
    Pillow (4.1.1)
    pip (9.0.1)
    protobuf (3.3.0)
    PyYAML (3.12)
    scipy (0.19.0)
    setuptools (28.8.0)
    six (1.10.0)
    tensorflow (1.1.0)
    Theano (0.9.0)
    Werkzeug (0.12.1)
    wheel (0.29.0)

