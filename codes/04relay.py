# --coding:utf-8--
"""
@author:marble
@file:04relay.py
@date:2021/8/24
继电器实验
"""
import time

import RPi.GPIO as GPIO

pin_switch = 17


class Switch:
    def __init__(self, pin_switch, *, initial=GPIO.LOW, mode=GPIO.BCM):
        self.pin_switch = pin_switch
        self.mode = mode
        self.initial = initial
        GPIO.setmode(self.mode)
        GPIO.setup(self.pin_switch, GPIO.OUT, initial=self.initial)

    def on(self):
        GPIO.output(self.pin_switch, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin_switch, GPIO.LOW)

    def switchstate(self):
        if self.state() == GPIO.LOW:
            self.on()
        else:
            self.off()

    def state(self):
        st = GPIO.input(self.pin_switch)
        print('state:', st)
        return st

    def cleanup(self):
        self.off()
        GPIO.cleanup(self.pin_switch)

    def __enter__(self):
        # print('with enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('with exit')
        self.cleanup()


if __name__ == '__main__':
    with Switch(pin_switch) as sw:
        while True:
            sw.switchstate()
            sw.state()
            print('-'*80)
            time.sleep(0.5)
