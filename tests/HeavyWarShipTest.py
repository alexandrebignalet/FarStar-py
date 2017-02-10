import unittest

from src.Blaster import Blaster
from src.Container import Container
from src.HeavyWarShip import HeavyWarShip
from src.Phaser import Phaser


class HeavyWarShipTest(unittest.TestCase):

    def setUp(self):
        self.vch = HeavyWarShip(100, 200, 3)

    def tearDown(self):
        self.vch = None

    def test_vch_can_load_any_weapons_and_only_weapons(self):
        with self.assertRaises(AssertionError):
            c = Container(1,1)
            self.assertRaises(AssertionError, self.vch.load(c))

            p = Phaser(1,1)
            b = Blaster(1,1,56)

            self.vch.load(p)
            self.vch.load(b)

            self.assertEqual(self.vch.equipments.index(p), 0)
            self.assertEqual(self.vch.equipments.index(b), 1)