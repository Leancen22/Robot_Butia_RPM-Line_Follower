#!/usr/bin/env python
import sys
import time
sys.path.insert(0, '/home/leandromesa/Desktop/TurtleBots.activity/plugins/butia')
from pybot import usb4butia
robot = usb4butia.USB4Butia()
start = time.time()
i = 0
while (i < 2000):
    robot.getDistance(5)
    i += 1
end = time.time()
timer = end - start
frecuency = i / timer
print(timer)
print(frecuency)