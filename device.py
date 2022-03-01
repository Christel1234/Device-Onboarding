from sim import *
from warehouse import *
from mockkeyinjection import *
from devicestate import *

class device:
    def __init__(self, serialID, isDamaged, flashed, keyinjected, needrepacking, IMEI):
        self.serialID = serialID
        self.isDamaged = isDamaged
        self.flashed = flashed
        self.keyinjected = keyinjected
        self.needrepacking = needrepacking 
        self.IMEI = IMEI

    def get_serialID(self):
        return self.serialID

    def set_packageID(self,box,crate):
        self.box = box
        self.crate = crate 
        self.state = devicestate.packageID_recorded
        return True
    def get_box(self):
        return self.box
    def get_crate(self):
        return self.crate


    def set_isDamaged(self):#maybe should change 
        if self.isDamaged:
            self.set_device_state("damage_recorded")
            self.flashed = None
            self.keyinjected = None
            self.needrepacking = None
            self.IMEI = None
    def get_isDamaged(self):
        return self.isDamaged

    def get_flashed(self):
        return self.flashed

    def get_keyinjected(self):
        return self.keyinjected

    def get_needrepacking(self):
        return self.needrepacking

    def set_IMEI(self,IMEI):
        self.IMEI = IMEI
        self.state = devicestate.imei_recorded
    def get_IMEI(self):
        return self.IMEI
##
    def set_device_state(self,state): 
        self.devicestate = state
    def get_device_state(self):
        return self.devicestate
##
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
"""
    def updatekeys(self, key):
        self.keyinjected = key
    def updateflashed(self):
        self.flashed = True
"""
newdevice = device(1,False,False,False,False,1)
newdevice.set_sim_info(1,1)
newdevice.set_warehouse_info(1,2,3,4,5,'BACK RIGHT')