import random
from datetime import datetime

class Breaker:
    def __init__(self, asset_id):
        self.asset_id = asset_id
        self.status = "OPEN"
        self.current = 0

    def update(self):
        if self.status =="CLOSED":
            self.current = random.randint(80, 150)
        else:
            self.current = 0 

    def get_telemetry(self):
        return {
            "asset_id": self.asset_id,
            "status": self.status,
            "current": self.current,
            "timestamp": datetime.now()

        }
    
    