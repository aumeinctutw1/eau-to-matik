from Relay import Relay
import time
from settings import RELAY_PIN, PUMP_OUPUT

class Pump():
    def __init__(self):
        self.relay = Relay(RELAY_PIN, False)
        self.outputCapacity = PUMP_OUPUT

    def water(self, volume):
        self.relay.on()
        time.sleep(self.getWateringDuration(volume))
        self.relay.off()

    def getWateringDuration(self, volume):
        #return volume / self.outputCapacity   
        return 10