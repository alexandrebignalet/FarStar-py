import unittest

from src.WarShip import WarShip
from src.Container import Container
from src.Equipment import Equipment
from src.Phaser import Phaser
from src.TransportShip import TransportShip


class EquipmentTest(unittest.TestCase):
    def setUp(self):
        self.phaser = Phaser(100, 200)
        self.container = Container(100, 200)
        self.transport_ship = TransportShip(100, 200, 90, 1000)

    def tearDown(self):
        self.transport_ship = None
        self.phaser = None
        self.container = None

    def test_equipment_constructor(self):

        self.assertEqual(self.phaser.name, "P-1")
        self.assertEqual(self.phaser.volume, 100)
        self.assertEqual(self.phaser.mass, 200)
        self.assertIsNone(self.phaser.location)

        self.assertEqual(self.container.name, "C-1")
        self.assertEqual(self.container.volume, 100)
        self.assertEqual(self.container.mass, 200)
        self.assertIsNone(self.container.location)

        self.assertEqual(self.transport_ship.name, "VT-1")
        self.assertEqual(self.transport_ship.volume, 100)
        self.assertEqual(self.transport_ship.mass, 200)
        self.assertIsNone(self.transport_ship.location)

    def test_equipment_location_can_only_be_a_ship_object(self):
        with self.assertRaises(ValueError):

            c = Container(1, 1)
            ts = TransportShip(10, 10, 9, 20)

            try:
                c.location = 10
            except ValueError as e:
                self.assertEqual(e.args, ('Any equipment must be load in a Ship.',))
                raise

            c.location = ts
            self.assertEqual(ts, c.location)