#from sense_hat import SenseHat
import time
import requests
import json


url = "http://192.168.1.117:3000/api/data"

#sense = SenseHat()

class Sensors:

    def update_sensor_data(self):
            temp = 69#temp = sense.get_temperature()
            hum = 5#hum = sense.get_humidity()
            ort = 6#ort = sense.get_gyroscope()
            return {'Temperature': temp, 'Humidity': hum, 'Orientation': ort}

    def write(self):
        time.sleep(1)
        return self.update_sensor_data()

data = Sensors()

while True:
    json_data = data.write()
    print(json_data)

headers = {"Content-Type": "application/json"}

# response = requests.post(url, data=data, headers=headers)
# print(response.text)






 