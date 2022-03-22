# pump
RELAY_PIN = 6
PUMP_OUPUT = 2000 / 60  # in ml/second

# ultrasonic sensor
GPIO_ECHO = 24
GPIO_TRIGGER = 18

# moisture sensor
REFERENCE_WET = 0
REFERENCE_DRY = 0

# moisture sensor i2c config
DEVICE_ADDRESS = 0x55
SET_REFERENCE_DRY = 0x44
SET_REFERENCE_WET = 0x55
GET_SOIL_MOISTURE = 0x76
GET_TEMPERATURE = 0x74

# personal settings
VOLUME_TO_WATER = 200  # in ml
MIN_WATER_LEVEL = 0  # in cm
MIN_SOIL_MOISTURE_LEVEL = 20 # in %
CONTAINER_VOLUME = 2400 # in ml
CONTAINER_HEIGHT = 24 # in cm
# distance from the ultrasonic sensor to the top of the container
# over the top of the container, then positive value
# under the top of the container, then negative value
ULTRASONIC_SENSOR_DISTANCE = -1 # in cm (negative value ok)

## InfluxDB
### these settings are specified in "docker-compose.yaml"
INFLUXDB_TOKEN = "iQYE83K9sUfEUslk3rQaf7mxsXbX3wO30b6eefPjnWvzG-H1JT7feg9CEsKMu7C3f2satvLrsHuKPm6c0aDukw=="
INFLUXDB_ORG = "eau-to-matik"
INFLUXDB_BUCKET = "eau-to-matik"
INFLUXDB_URL = "http://localhost:8086"
