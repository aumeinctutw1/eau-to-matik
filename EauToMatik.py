from MoistureSensor import MoistureSensor
from WaterLevelController import WaterLevelController
from Pump import Pump
from settings import MIN_SOIL_MOISTURE_LEVEL

class EauToMatik():
    def __init__(self):
        self.Pump = Pump()
        self.WaterLevelController = WaterLevelController()
        self.MoistureSensor = MoistureSensor()

    def run(self):
        if (self.soilIsDry() and self.WaterLevelController.hasEnoughWater()):
            self.Pump.water()

    def soilIsDry(self):
        return self.MoistureSensor.getAvgMoistureLevel() < MIN_SOIL_MOISTURE_LEVEL




