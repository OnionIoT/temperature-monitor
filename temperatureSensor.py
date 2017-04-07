from oneWire import OneWire

# main class definition
class TemperatureSensor:
    def __init__(self, interface, args):
        self.supportedInterfaces = ["oneWire"]
        self.interface = interface
        self.ready = False

        # if specified interface not supported
        if self.interface not in self.supportedInterfaces:
            print "Unsupported interface."
            self.listInterfaces()
            return

        # set up a driver based on the interface type
        # you can extend this class by adding more drivers! (eg. serial, I2C, etc)
        if self.interface == "oneWire":
            self.driver = OneWire(args.get("address"), args.get("gpio", None))
            # signal ready status
            self.ready = self.driver.setupComplete
            # match the return value to
            self.readValue = self.__readOneWire;

    def listInterfaces(self):
        print "The supported interfaces are:"
        for interface in self.supportedInterfaces:
            print interface

    # read one-wire devices
    def __readOneWire(self):
        # device typically prints 2 lines, the 2nd line has the temperature sensor at the end
        # eg. a6 01 4b 46 7f ff 0c 10 5c t=26375
        rawValue = self.driver.readDevice()

        # grab the 2nd line, then read the last entry in the line, then get everything after the "=" sign
        value = rawValue[1].split()[-1].split("=")[1]

        # convert value from string to number
        value = int(value)

        # DS18B20 outputs in 1/1000ths of a degree C, so convert to standard units
        value /= 1000.0
        return value

    # add more __read() functions for different interface types later!