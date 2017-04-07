import os
import json
import oneWire
import temperatureSensor
import ubidots
# import config
dirName = os.path.dirname(os.path.abspath(__file__))
# read the config file relative to the script location
with open( '/'.join([dirName, 'config.json']) ) as f:
    config = json.load(f)

token = config["token"]
deviceName = config["deviceName"]
oneWireGpio = 19

def __main__():
    device = ubidots.UbidotsDevice(token, deviceName)

    if not oneWire.setupOneWire(str(oneWireGpio)):
        print "Kernel module could not be inserted. Please reboot and try again."
        return -1

    # get the address of the temperature sensor
    # 	it should be the only device connected in this experiment    
    sensorAddress = oneWire.scanOneAddress()

    # instantiate the temperature sensor object
    sensor = temperatureSensor.TemperatureSensor("oneWire", { "address": sensorAddress, "gpio": oneWireGpio })
    if not sensor.ready:
        print "Sensor was not set up correctly. Please make sure that your sensor is firmly connected to the GPIO specified above and try again."
        return -1

    # check and print the temperature
    value = sensor.readValue()
    dataPoint = {
        "temperature": value
    }
    device.pushDataPoint(dataPoint)
    print dataPoint

if __name__ == '__main__':
    __main__()