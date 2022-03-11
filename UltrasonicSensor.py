import time
import RPi.GPIO as GPIO
from settings import GPIO_ECHO, GPIO_TRIGGER

class UltrasonicSensor():
    def __init__(self):
        self.triggerPin = GPIO_TRIGGER
        self.echoPin = GPIO_ECHO
        GPIO.setmode(GPIO.BCM)
        # set GPIO direction (IN / OUT)
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)

    def getDistance(self):
        # set Trigger to HIGH
        GPIO.output(self.triggerPin, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.triggerPin, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(self.echoPin) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(self.echoPin) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance