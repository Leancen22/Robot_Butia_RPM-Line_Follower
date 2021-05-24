#!/usr/bin/env python
import sys
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0, '/home/leandromesa/Desktop/TurtleBots.activity/plugins/butia')
from pybot import usb4butia
robot = usb4butia.USB4Butia()
rpm_values = []
speeds = []
for speed in range(400, 1023, 50):
        speeds.append(speed)
for i in speeds:
        sample = 0
        robot.set2MotorSpeed(0, i, 0, i)
        start = time.time()
        while (sample < 150):
                if (robot.getGray(5) < 19350):
                        sample += 1
        end = time.time()
        timeer = (end - start)
        rpm = 60/timeer
        rpm_values.append(rpm)
robot.set2MotorSpeed(0, 0, 0, 0)

x = speeds
y = rpm_values
fig,ax = plt.subplots() 
ax.plot(x, y) 
plt.show()

