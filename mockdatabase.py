from device import *

class mockdatabase:
    def __init__(self):
        self.DeviceList = []

    def newDevice(self,serialID,boxID,crateID,isDamaged,IMEI):
        self.DeviceList.append(device(serialID,boxID,crateID,isDamaged,IMEI)) 

database = mockdatabase()
database.newDevice(1,1,1,False,1)

       