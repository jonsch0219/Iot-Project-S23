import machine
import adafruit
led = machine.Pin(1, machine.Pin.OUT)   # led pin initialization for Raspberry Pi Pico W

def checkMaxTemp(temp):
    if temp > adafruit.templimit:
        led.high()
        return "ON"
    led.low()
    return "OFF"