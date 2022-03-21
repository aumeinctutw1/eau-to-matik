from settings import RELAY_PIN
import RPi.GPIO as GPIO
import time

class Relay():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RELAY_PIN, GPIO.OUT)

    def on(self):
        GPIO.output(RELAY_PIN, True)

    def off(self):
        GPIO.output(RELAY_PIN, False)
        