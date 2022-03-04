import unittest
from mockdatabase import *
from device import *

class testDeviceOnboarding(unittest.TestCase):
    def testNewDeviceInfo(self):
        self.assertEqual(newdevice.get_serialID(),1)
        self.assertEqual(newdevice.get_box(),1)
        self.assertEqual(newdevice.get_crate(),1)
        self.assertEqual(newdevice.get_isDamaged(),False)
        self.assertEqual(newdevice.get_IMEI(),1)

    def testSimCard(self):
        self.assertEqual(newdevice.get_sim_snn(),1)
        self.assertEqual(newdevice.get_sim_imsi(),1)
    
    def testWarehouse(self):
        self.assertEqual(newdevice.get_warehouse_number(),1)
        self.assertEqual(newdevice.get_section_number(),2)
        self.assertEqual(newdevice.get_row_number(),3)
        self.assertEqual(newdevice.get_shelf_number(),4)
        self.assertEqual(newdevice.get_segment_number(),5)
        self.assertEqual(newdevice.get_segment_section(),'BACK RIGHT')

    def testAddedDeviceToDatabase(self):
        self.assertEqual(database.get_length(),1)

 #   def testDeviceStateUpdated(self):
  #      self.assertEqual(newdevice.get_device_state(), "warehouse_stored")

"""
    def testFindBySerialID(self):
        self.assertEqual(database.get_device_by_serialID(123),mydevice)

    def testFindByIMEI(self):
        self.assertEqual(database.get_device_by_IMEI(321),mydevice)
    
    #def test

"""
if __name__ == "__main__":
    unittest.main()