from sim import *

class device:
    def __init__(self, serialID, boxID, crateID, isDamaged, IMEI):
        self.serialID = serialID
        self.boxID = boxID
        self.crateID = crateID
        self.isDamaged = isDamaged
        self.IMEI = IMEI
    def get_serialID(self):
        return self.serialID
    def get_boxID(self):
        return self.boxID
    def get_crateID(self):
        return self.crateID
    def get_isDammaged(self):
        return self.isDamaged
    def get_IMEI(self):
        return self.IMEI
    
    def set_sim_info(self,SNN,IMSI):
        self.SNN = SNN
        self.IMSI = IMSI
    def get_sim_snn(self):
        return self.SNN
    def get_sim_imsi(self):
        return self.IMSI
    
newdevice = device(1,1,1,False,1)
newdevice.set_sim_info(1,1)