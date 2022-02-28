from device import *

class mockdatabase:
    def __init__(self):
        self.deviceList = []

    def get_length(self):
        return len(self.deviceList)

    def append_device(self,mydevice):
        self.deviceList.append(mydevice) 


    def get_device_by_serialID(self, serialID):
        for currentdevice in self.deviceList:
            if device.get_serialID == serialID:
                return currentdevice

    def get_device_by_IMEI(self, IMEI):
        for currentdevice in self.deviceList:
            if device.get_IMEI == IMEI:
                return currentdevice
                
database = mockdatabase()
database.append_device(newdevice)