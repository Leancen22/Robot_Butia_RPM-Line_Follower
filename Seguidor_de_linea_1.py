#!/usr/bin/env python
import sys
import time
sys.path.insert(0, '/home/leandromesa/Desktop/TurtleBots.activity/plugins/butia')
from pybot import usb4butia
robot = usb4butia.USB4Butia()
while (True):
    robot.set2MotorSpeed(0, 1023, 0, 1023)
    if (robot.getGray(1) > 52000):
        robot.set2MotorSpeed(0, 0, 0, 350)
        time.sleep(0.3)