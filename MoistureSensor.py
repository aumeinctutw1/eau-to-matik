import smbus
import time
from settings import REFERENCE_DRY, REFERENCE_WET, SET_REFERENCE_DRY, SET_REFERENCE_WET, DEVICE_ADDRESS, GET_SOIL_MOISTURE, GET_TEMPERATURE

class MoistureSensor():
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
        try:
            moisture = self.bus.read_i2c_block_data(DEVICE_ADDRESS, GET_SOIL_MOISTURE, 2)
        except Exception as e:
            print(type(e))
            measuredMoisture = 0
        measuredMoisture = round(moisture[1]/2.55, 1)
        return measuredMoisture

    # gets the avg value, last 30 seconds
    def getAvgMoistureLevel(self):
        try: 
            moisture = self.bus.read_i2c_block_data(DEVICE_ADDRESS, GET_SOIL_MOISTURE, 2)
        except Exception as e:
            print(type(e))
            avgMoisture = 0

        avgMoisture = round(moisture[0]/2.55, 1)
        return avgMoisture

    def getSoilTemperature(self):
        temp = self.bus.read_byte_data(DEVICE_ADDRESS, GET_TEMPERATURE)
        return temp