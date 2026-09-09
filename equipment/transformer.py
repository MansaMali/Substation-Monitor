import random
from datetime import datetime

class Transformer:
    def __init__(self, asset_id):
        self.asset_id = asset_id

        self.voltage = 7200

        self.current = 120

        self.temperature = 65

        self.load_percent = 50

    def update(self):
        self.voltage += random.randint(-15,15)

        self.current += random.randint(-3,3)

        self.temperature += random.randint(-10, 30)

        self.load_percent += random.randint(-10, 50)

    def get_telemetry(self):
            return {
                "asset_id": self.asset_id,
                "voltage": self.voltage,
                "current": self.current,
                "temperature": self.temperature,
                "load_percent": self.load_percent,
                "timestamp": datetime.now()
    
            }