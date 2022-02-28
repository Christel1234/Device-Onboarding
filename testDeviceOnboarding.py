import unittest
from mockdatabase import *
from device import *

class testDeviceOnboarding(unittest.TestCase):
    def testNewDeviceInfo(self):
        self.assertEqual(newdevice.serialID,1)
        self.assertEqual(newdevice.boxID,1)
        self.assertEqual(newdevice.crateID,1)
        self.assertEqual(newdevice.isDamaged,False)
        self.assertEqual(newdevice.IMEI,1)

    def testSimCard(self):
        self.assertEqual(newdevice.siminfo.SNN,1)
        self.assertEqual(newdevice.siminfo.IMSI,1)

    
    def testAddDevice(self):
        pass
    

if __name__ == "__main__":
    unittest.main()