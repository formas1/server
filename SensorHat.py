from sense_hat import SenseHat
import time
import requests
import json


url = "http://192.168.1.117:3000/api/data"

sense = SenseHat()

class Sensors():

    def update_sensor_data(self):
            temp = sense.get_temperature()
            hum = sense.get_humidity()
            ort = sense.get_gyroscope()
            return {'Temperature': temp, 'Humidity': hum, 'Orientation': ort}

    def write():
        while True:
            json_data = json.dumps(Sensors.update_sensor_data)
            time.sleep(5)

data = Sensors.write()

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=data, headers=headers)
print(response.text)






 