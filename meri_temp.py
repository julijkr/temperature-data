import json
import datetime
import os

import time
import board
import adafruit_dht

dht = adafruit_dht.DHT22(board.D4)

try:
	while True:
		try:
			temperature = dht.temperature
			podatki = {
				"temperatura": round(temperature, 1),
				"cas": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			}
			with open("podatki.json", "w") as datoteka:
				json.dump(podatki, datoteka)
			print("Temperatura:", podatki["temperatura"], "°C")
		except:
			print("Napaka")
		time.sleep(2)
		
except KeyboardInterrupt:
	print("Konec")

finally: 
	dht.exit()



with open("podatki.json", "w") as datoteka:
    json.dump(podatki, datoteka)

print("Temperatura:", podatki["temperatura"], "°C")
#import time
#import board
#import adafruit_dht

#dht = adafruit_dht.DHT22(board.D4)

#try:
#	while True:
#		try:
#			temperature = dht.temperature
#			print(temperature)
#		except:
#			print("Napaka")
#		time.sleep(2)

#except KeyboardInterrupt:
#	print("Konec")

#finally: 
#	dht.exit()
