class mockdevice:
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

    
        

    