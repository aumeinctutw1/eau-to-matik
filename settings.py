# pump
RELAY_PIN = 12
PUMP_OUPUT = 1200 / 3600  # in ml/second

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
MIN_WATER_LEVEL = 5  # in cm
MAX_WATER_LEVEL = 20  # high position of ultrasonic sensor
