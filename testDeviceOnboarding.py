import unittest
from mockdatabase import *
from mockdevice import *

class testDeviceOnboarding(unittest.TestCase):
    def testNewDeviceInfo(self):
        self.assertEqual(device.serialID,1)
        self.assertEqual(device.boxID,1)
        self.assertEqual(device.crateID,1)
        self.assertEqual(device.isDamaged,False)
        self.assertEqual(device.IMEI,1)

    def testSimCard(self):
        self.assertEqual(device.siminfo.SNN,1)
        self.assertEqual(device.siminfo.IMSI,1)

    

if __name__ == "__main__":
    unittest.main()