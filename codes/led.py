# --coding:utf-8--


import RPi
import RPi.GPIO as GPIO
import time


class Led:
    def __init__(self, pin, *, initial=GPIO.LOW, mode=GPIO.BCM, freq: 'Hz' = 100, light: 'light percent' = 100):
        self.pin = pin
        self.freq = freq
        self.light = light
        self.initial = initial
        self.mode = mode
        GPIO.setmode(mode)
        GPIO.setup(self.pin, GPIO.OUT, initial=initial)
        self.led = GPIO.PWM(self.pin, self.freq)

    def __repr__(self):
        return f'''Led(pin={self.pin},initial={self.initial},mode={self.mode},freq={self.freq},light={self.light})'''

    def on(self, light: "light percent" = None):
        if light is not None:
            self.light = light
        self.led.start(self.light)

    def off(self):
        self.led.stop()

    def cleanup(self):
        self.off()
        GPIO.cleanup(self.pin)

    def __enter__(self):
        # print('with enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('with exit')
        self.cleanup()


class MultiColorLed:
    def __init__(self, pins, **kwargs):
        self.pins = pins
        # print(kwargs)
        # self.leds = tuple(Led(pin) for pin in self.pins)
        self.leds = self.getleds(pins, **kwargs)

    @staticmethod
    def getleds(pins, **kwargs):
        leds = []
        for i in range(len(pins)):
            pin = pins[i]
            kws = {}
            for k, v in kwargs.items():
                if i >= len(v):
                    continue
                kws.update({k: v[i]})
            # print('pin',pin)
            # print('kws:',kws)
            leds.append(Led(pin, **kws))
        return tuple(leds)

    def setcolors(self, colors: "0xAABB" = None):
        if colors is None:
            return None
        lights = self.colors2lights(colors)
        print(lights)
        for led, light in zip(self.leds, lights):
            led.on(light)

    def colors2lights(self, colors):
        color_list = []
        for i in range(len(self.pins)):
            color_list.append(colors & 0xff)
            colors >>= 8
        color_list.reverse()
        lights = [color / 255 * 100 for color in color_list]
        return lights

    def cleanup(self):
        for led in self.leds:
            led.cleanup()
        # GPIO.cleanup(self.pins)

    def __enter__(self):
        # print('with enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('with exit')
        self.cleanup()


pin_G = 18
pin_R = 17
pin_B = 27
if __name__ == '__main__':
    # 呼吸灯
    # led = Led(pin_R)
    # led__G = Led(pin_G)
    # led__G.on()
    with Led(pin_B) as led:
        while True:
            for i in range(100):
                led.on(i)
                # print(f"light: {i}%")
                time.sleep(0.01)
            time.sleep(0.4)
            for i in range(100, 0, -1):
                led.on(i)
                # print(f"light: {i}%")
                time.sleep(0.01)
            time.sleep(0.4)
        # input('enter to exit:')
