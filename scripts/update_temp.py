import Adafruit_DHT
import json
from datetime import datetime

sensor = Adafruit_DHT.DHT22
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

data = {
    "temperature": round(temperature, 1),
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "location": "Ljubljana"
}

with open("data/temperature.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"Temperature updated: {data['temperature']}°C")
