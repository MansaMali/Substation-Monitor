import random
from datetime import datetime

class CapacitorBank:
    def __init__(self, asset_id):
        self.asset_id = asset_id
        self.status = "OFF"
        self.reactive_power = 0

    def update(self):
        if self.status =="ON":
            self.reactive_power = random.randint(500,1000)
        else:
            self.reactive_power = 0
    def get_telemetry(self):
                return {
                    "asset_id": self.asset_id,
                    "status" : self.status,
                    "reactive_power" : self.reactive_power,
                    "timestamp": datetime.now()
        
                }