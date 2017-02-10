import unittest

from src.Container import Container
from src.HybridShip import HybridShip
from src.Phaser import Phaser
from src.TransportShip import TransportShip


class HybridShipTest(unittest.TestCase):

    def setUp(self):
        self.hs = HybridShip(100, 200, 90, 2000, 2)

    def tearDown(self):
        self.hs = None

    def test_hybrid_can_load_any_equipment(self):
        c = Container(1,1)
        p = Phaser(1,1)
        ts = TransportShip(10,20,9,34)

        self.hs.load(c)
        self.hs.load(p)
        self.hs.load(ts)

        self.assertEqual(self.hs.equipments.index(c), 0)
        self.assertEqual(self.hs.equipments.index(p), 1)
        self.assertEqual(self.hs.equipments.index(ts), 2)

    def test_hybrid_can_equip_max_nb_weapons_only(self):
        with self.assertRaises(AssertionError):
            p = Phaser(1,1)
            p1 = Phaser(1,1)
            p2 = Phaser(1,1)

            self.hs.equip(p)
            self.hs.equip(p1)

            self.assertRaises(AssertionError, self.hs.equip(p2))

            self.hs.unequip(p1)
            self.assertEqual(len(self.hs.equipments), 1)