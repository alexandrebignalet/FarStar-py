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

    def test_blaster_gaz_level_must_be_a_percent(self):
        with self.assertRaises(AssertionError):
            self.assertRaises(Blaster(1, 1, 1000))
            self.assertRaises(Blaster(1, 1, -43))