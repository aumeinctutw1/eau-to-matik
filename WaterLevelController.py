from UltrasonicSensor import UltrasonicSensor
from settings import MIN_WATER_LEVEL, ULTRASONIC_SENSOR_DISTANCE, CONTAINER_HEIGHT, CONTAINER_VOLUME, VOLUME_TO_WATER

class WaterLevelController():
    def __init__(self):
        self.UltraSonicSensor = UltrasonicSensor()
        self.minWaterLevel = MIN_WATER_LEVEL
        self.pos = ULTRASONIC_SENSOR_DISTANCE

    def getVolumeWaterInContainer(self):
        distanceToWater = self.UltraSonicSensor.getDistance()
        distanceTopContainerToWater = distanceToWater - self.pos
        waterLevel = CONTAINER_HEIGHT - distanceTopContainerToWater
        volumeWater = (waterLevel / CONTAINER_HEIGHT) * CONTAINER_VOLUME
        
        return volumeWater

    def getWaterLevelInProcent(self):
        return self.getVolumeWaterInContainer() / CONTAINER_VOLUME * 100
        
    def hasEnoughWater(self):
        return self.getVolumeWaterInContainer() > VOLUME_TO_WATER
