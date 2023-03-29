import requests
import json
import time
from sense_hat import SenseHat

sense = SenseHat()
# set the API endpoint URL
url = "http://192.168.1.117:3000/api/data"

def updateData():
    # define the data you want to send in JSON format
    data = {
        "Temperature": sense.temp,
        "Humidity": sense.humidity,
        "Pressure": sense.pressure,
        "Orientation": sense.orientation,
        "Gyro": sense.gyro,
        "Accelerometer": sense.accel,
        "Compass": sense.compass
    }

    # convert the data to a JSON string
    json_data = json.dumps(data)

    # set the headers to indicate that we are sending JSON data
    headers = {"Content-Type": "application/json"}

    # make the POST request
    response = requests.post(url, data=json_data, headers=headers)

    # print the response from the server
    print(response.text)

while True:
    updateData()
    time.sleep(100)
    
