# --coding:utf-8--
"""
@author:marble
@file:rgbled.py
@date:2021/8/22
"""

from led import MultiColorLed
import RPi.GPIO as GPIO
import time


class RGBLed(MultiColorLed):
    pass


pin_R = 17
pin_G = 18
pin_B = 27
colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF,0xffffff]
if __name__ == '__main__':
    freq=(2000, 1999, 5000)
    with RGBLed((pin_R, pin_G, pin_B)) as rgbled:
        for color in colors:
            print("color:",hex(color))
            rgbled.setcolors(color)
            time.sleep(1)

    pass
