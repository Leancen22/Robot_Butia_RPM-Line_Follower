#!/usr/bin/env python
import sys
import time
sys.path.insert(0, '/home/leandromesa/Desktop/TurtleBots.activity/plugins/butia')
from pybot import usb4butia
robot = usb4butia.USB4Butia()
while (True):
    robot.set2MotorSpeed(1, 1023, 1, 1023)
    while (robot.getGray(5) < 49000):
        robot.set2MotorSpeed(1, 0, 1, 350)
    while (robot.getGray(1) < 39000):
        robot.set2MotorSpeed(1, 350, 1, 0)

