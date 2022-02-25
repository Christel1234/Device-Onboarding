import unittest
from mockdatabase import *
from mockdevice import *

class testDeviceOnboarding(unittest.TestCase):
    def testNewDevice(self):
        device = mockdevice(1,1,1,False,1)
        self.assertEqual(device.serialID,1)
        self.assertEqual(device.boxID,1)
        self.assertEqual(device.crateID,1)
        self.assertEqual(device.isDamaged,False)
        self.assertEqual(device.IMEI,1)

if __name__ == "__main__":
    unittest.main()