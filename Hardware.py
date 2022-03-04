from gpiozero import OutputDevice
import RPi.GPIO as GPIO
import time
import smbus
from Hardware import Hardware
from settings import GET_TEMPERATURE, RELAY_PIN, PUMP_OUPUT, DEVICE_ADDRESS, SET_REFERENCE_WET, SET_REFERENCE_DRY, GET_SOIL_MOISTURE, REFERENCE_DRY, REFERENCE_WET, GPIO_ECHO, GPIO_TRIGGER, MIN_WATER_LEVEL, MAX_WATER_LEVEL


class EauToMatik():
    def __init__(self):
        self.Pump = Pump()
        self.WaterLevelController = WaterLevelController()

    def run(self):
        if (self.WaterLevelController.hasEnoughWater()):
            self.Pump.water()


class moistureSensor():
    def __init__(self):
        # init the bus
        DEVICE_BUS = 1
        self.bus = smbus.SMBus(DEVICE_BUS)

        # configure sensor with reference values, if not set -> default values provided by sensor
        if REFERENCE_WET:
            self.bus.write_word_data(DEVICE_ADDRESS, SET_REFERENCE_WET, REFERENCE_WET)
            time.sleep(0.2)

        if REFERENCE_DRY:
            self.bus.write_word_data(DEVICE_ADDRESS, SET_REFERENCE_DRY, REFERENCE_DRY)
            time.sleep(0.2)

    # gets the directly measured value
    def getMoistureLevel(self):
        moisture = self.bus.read_i2c_block_data(DEVICE_ADDRESS, GET_SOIL_MOISTURE, 2)
        measuredMoisture = round(moisture[1]/2.55, 1)
        return measuredMoisture

    # gets the avg value, last 30 seconds
    def getAvgMoistureLevel(self):
        moisture = self.bus.read_i2c_block_data(DEVICE_ADDRESS, GET_SOIL_MOISTURE, 2)
        avgMoisture = round(moisture[0]/2.55, 1)
        return avgMoisture

    def getTemperature(self):
        temp = self.bus.read_byte_data(DEVICE_ADDRESS, GET_TEMPERATURE)
        return temp


class Relay(OutputDevice):
    def __init__(self, pin, active_high):
        super(Relay, self).__init__(pin, active_high)


class Pump():
    def __init__(self):
        self.relay = Hardware.Relay(RELAY_PIN, False)
        self.outputCapacity = PUMP_OUPUT

    def water(self, volume):
        self.relay.on()
        time.sleep(self.getWateringDuration(volume))
        self.relay.off()

    def getWateringDuration(self, volume):
        return volume / self.outputCapacity


class WaterLevelController():
    def __init__(self):
        self.UltraSonicSensor = Hardware.UltrasonicSensor()
        self.minWaterLevel = MIN_WATER_LEVEL
        self.maxWaterLevel = MAX_WATER_LEVEL

    def hasEnoughWater(self):
        return self.UltrasonicSensor.getDistance() < self.maxWaterLevel - self.minWaterLevel


class UltrasonicSensor(GPIO):
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
