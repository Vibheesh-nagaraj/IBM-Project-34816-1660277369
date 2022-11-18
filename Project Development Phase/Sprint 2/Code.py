#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
myConfig = {
    "identity": {
        "orgId": "ede5q6",
        "typeId": "Locator",
        "deviceId":"54321"
    },
    "auth": {
        "token": "-DO!)E9jNUw7gpC57O"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    city = "London"
    lat = 34.8976508
    long = 67.9764532

    data = {'name':city, 'lat':lat, 'lon':long}
    client.publishEvent(eventId="Active", msgFormat="json", data=data, qos=0, onPublish=None)
    print("Data Updated to IBM Platform: ", data)
    time.sleep(3)
client.disconnect()