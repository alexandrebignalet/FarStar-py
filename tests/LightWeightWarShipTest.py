import unittest

from src.Blaster import Blaster
from src.LightWeightWarShip import LightWeightWarShip
from src.Phaser import Phaser


class LightWeightWarShipTest(unittest.TestCase):

    def setUp(self):
        self.vcl = LightWeightWarShip(10, 20, 3)

    def tearDown(self):
        self.vcl = None

    def test_light_weight_war_ship_can_load_only_phasers(self):
        with self.assertRaises(AssertionError):
            p = Phaser(1, 1)
            b = Blaster(1, 1, 45)

            self.vcl.load(p)
            self.assertEqual(len(self.vcl.equipments), 1)
            self.assertRaises(AssertionError, self.vcl.load(b))
