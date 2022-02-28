from sim import *
from warehouse import *

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

    def set_warehouse_info(self,warehouse_number,section_number,row_number,shelf_number,segment_number,segment_section):
        self.warehouse_number = warehouse_number
        self.section_number = section_number
        self.row_number = row_number
        self.shelf_number = shelf_number
        self.segment_number = segment_number
        self.segment_section = segment_section
    def get_warehouse_number(self):
        return self.warehouse_number
    def get_section_number(self):
        return self.section_number
    def get_row_number(self):
        return self.row_number
    def get_shelf_number(self):
        return self.shelf_number
    def get_segment_number(self):
        return self.segment_number
    def get_segment_section(self):
        return self.segment_section
    
newdevice = device(1,1,1,False,1)
newdevice.set_sim_info(1,1)
newdevice.set_warehouse_info(1,2,3,4,5,6)