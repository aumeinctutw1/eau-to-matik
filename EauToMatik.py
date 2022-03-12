from MoistureSensor import MoistureSensor
from WaterLevelController import WaterLevelController
from Pump import Pump
from settings import MIN_SOIL_MOISTURE_LEVEL, VOLUME_TO_WATER

class EauToMatik():
    def __init__(self):
        self.Pump = Pump()
        self.WaterLevelController = WaterLevelController()
        self.MoistureSensor = MoistureSensor()

    def run(self):
        if (self.soilIsDry() and self.WaterLevelController.hasEnoughWater(VOLUME_TO_WATER)):
            self.Pump.water()

    def soilIsDry(self):
        return self.MoistureSensor.getAvgMoistureLevel() < MIN_SOIL_MOISTURE_LEVEL




