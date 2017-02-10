import unittest

from src.Blaster import Blaster


class BlasterTest(unittest.TestCase):

    def setUp(self):
        self.b = Blaster(10,10,54)

    def test_constructor(self):
        self.assertEqual(self.b.gaz_level, 54)

    def test_recharge_method(self):
        self.assertEqual(self.b.gaz_level, 54)
        self.b.recharge()
        self.assertEqual(self.b.gaz_level, 100)