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

if __name__ == "__main__":
    unittest.main()