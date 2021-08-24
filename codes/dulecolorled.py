# --coding:utf-8--
"""
@author:marble
@file:dulecolorled.py
@date:2021/8/21
"""
import time

import RPi.GPIO as GPIO
from led import MultiColorLed


class DuleColorLed(MultiColorLed):
    pass


pin_R = 17
pin_G = 18
colors = [0xff00, 0xf00f, 0x0ff0, 0x00ff, 0x60ff, None]
if __name__ == '__main__':

    with DuleColorLed([pin_R, pin_G], freq=(2000,)) as dled:
        print(dled.leds)
        for color in colors:
            print('color:', color)
            dled.setcolors(color)
            time.sleep(1)
    pass
