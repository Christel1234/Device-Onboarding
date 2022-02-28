from device import *

class mockdatabase:
    def __init__(self):
        self.deviceList = []

    def get_length(self):
        return len(self.deviceList)

    def append_device(self,mydevice):
        self.deviceList.append(mydevice) 

database = mockdatabase()
database.append_device(newdevice)
