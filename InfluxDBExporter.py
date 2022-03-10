from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from settings import INFLUXDB_URL, INFLUXDB_TOKEN, INFLUXDB_ORG, INFLUXDB_BUCKET

class InfluxDBExporter:
    def __init__(self):
        self.url = INFLUXDB_URL
        self.token = INFLUXDB_TOKEN
        self.org = INFLUXDB_ORG
        self.bucket = INFLUXDB_BUCKET

    def exportMoistureLevel(self, moistureLevel):
        with InfluxDBClient(url=self.url, token=self.token, org=self.org) as client:
            write_api = client.write_api(write_options=SYNCHRONOUS)
            moisture = Point("soil") \
                .tag("device", "moisture1") \
                .field("moisture_percent", moistureLevel) \
                .time(datetime.utcnow(), WritePrecision.NS)
            write_api.write(self.bucket, self.org, moisture)
            client.close()

    def exportSoilTemperature(self, soilTemp):
        with InfluxDBClient(url=self.url, token=self.token, org=self.org) as client:
            write_api = client.write_api(write_options=SYNCHRONOUS)
            temp = Point("soil") \
                .tag("device", "moisture1") \
                .field("temp_celsius", soilTemp) \
                .time(datetime.utcnow(), WritePrecision.NS)
            write_api.write(self.bucket, self.org, temp)
            client.close()

    def exportWaterLevel(self, waterLevel):
        with InfluxDBClient(url=self.url, token=self.token, org=self.org) as client:
            write_api = client.write_api(write_options=SYNCHRONOUS)
            water = Point("water") \
                .tag("device", "ultrasonic1") \
                .field("water_level_percent", waterLevel) \
                .time(datetime.utcnow(), WritePrecision.NS)
            write_api.write(self.bucket, self.org, water)
            client.close()

    def exportPumpedWater(self, pumpedWater):
        with InfluxDBClient(url=self.url, token=self.token, org=self.org) as client:
            write_api = client.write_api(write_options=SYNCHRONOUS)
            water = Point("water") \
                .tag("device", "pump1") \
                .field("pumped_water_ml", pumpedWater) \
                .time(datetime.utcnow(), WritePrecision.NS)
            write_api.write(self.bucket, self.org, water)
            client.close()