import subprocess
import json

class UbidotsDevice:
    def __init__(self, token, deviceName):
        self.token = token
        self.deviceName = deviceName
        self.baseCommand = ["ubidots", "-t", token, "-d", deviceName]
    
    # send json objects from a list
    def pushDataPoint(self, dataPoint):
        dataJson = json.dumps(dataPoint)
        command = self.baseCommand
        command.extend(["set", dataJson])
        subprocess.call(command)