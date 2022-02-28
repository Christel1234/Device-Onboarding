import unittest
from mockdatabase import *
from device import *

class testDeviceOnboarding(unittest.TestCase):
    def testNewDeviceInfo(self):
        self.assertEqual(newdevice.get_serialID(),1)
        self.assertEqual(newdevice.get_boxID(),1)
        self.assertEqual(newdevice.get_crateID(),1)
        self.assertEqual(newdevice.get_isDammaged(),False)
        self.assertEqual(newdevice.get_IMEI(),1)

    def testSimCard(self):
        self.assertEqual(newdevice.get_sim_snn(),1)
        self.assertEqual(newdevice.get_sim_imsi(),1)

    def testAddedDeviceToDatabase(self):
        self.assertEqual(database.get_length(),1)

    def testWarehouse(self):
        self.assertEqual(newdevice.get_warehouse_number(),1)
        self.assertEqual(newdevice.get_section_number(),2)
        self.assertEqual(newdevice.get_row_number(),3)
        self.assertEqual(newdevice.get_shelf_number(),4)
        self.assertEqual(newdevice.get_segment_number(),5)

        self.assertEqual(newdevice.get_segment_section(),'BACK RIGHT')

    def testFindBySerialID(self):
        mydevice = device(123,1,1,False,321)
        mydatabase = mockdatabase()
        mydatabase.append_device(mydevice)
        self.assertEqual(database.get_device_by_serialID(123),mydevice)

    def testFindByIMEI(self):
        mydevice = device(123,1,1,False,321)
        mydatabase = mockdatabase()
        mydatabase.append_device(mydevice)
        self.assertEqual(database.get_device_by_IMEI(321),mydevice)

if __name__ == "__main__":
    unittest.main()