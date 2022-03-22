from MoistureSensor import MoistureSensor
from WaterLevelController import WaterLevelController
from InfluxDBExporter import InfluxDBExporter
from Pump import Pump
from settings import MIN_SOIL_MOISTURE_LEVEL, VOLUME_TO_WATER


class EauToMatik():
    def __init__(self):
        self.Pump = Pump()
        self.WaterLevelController = WaterLevelController()
        self.MoistureSensor = MoistureSensor()
        self.Exporter = InfluxDBExporter()

    def run(self):
        self.saveDataFromSensors()

        # check if watering is necessary
        if (self.soilIsDry() and self.WaterLevelController.hasEnoughWater()):
            # activate pump
            self.Pump.water(VOLUME_TO_WATER)
            # save volume of water given to plant
            self.Exporter.exportPumpedWater(VOLUME_TO_WATER)
            self.saveDataFromSensors()

    def soilIsDry(self):
        return self.MoistureSensor.getAvgMoistureLevel() < MIN_SOIL_MOISTURE_LEVEL

    def saveDataFromSensors(self):
        # save moisture and temperature in DB
        self.Exporter.exportMoistureLevel(
            self.MoistureSensor.getAvgMoistureLevel())
        self.Exporter.exportSoilTemperature(
            self.MoistureSensor.getSoilTemperature())
        # save water level in tank
        self.Exporter.exportWaterLevel(
            self.WaterLevelController.getWaterLevelInProcent())
        self.Exporter.exportEnoughWater(
            1 if self.WaterLevelController.hasEnoughWater() else 0
        )
