import unittest

from src.Container import Container
from src.Phaser import Phaser
from src.TransportShip import TransportShip
from src.WarShip import WarShip


class EquipmentTest(unittest.TestCase):
    def setUp(self):
        self.transport_ship = TransportShip(100, 200, 90, 1000)
        self.war_ship = WarShip(100, 200, 5)

    def tearDown(self):
        self.transport_ship = None
        self.war_ship = None

    def test_mass_must_be_the_mass_sum_of_all_the_equipments_loaded_plus_the_transport_ship_mass(self):

        c = Container(1,1)

        base_mass = self.transport_ship.mass

        self.transport_ship.load(c)

        self.assertGreater(self.transport_ship.mass, base_mass)

        self.assertEqual(self.transport_ship.mass, base_mass + c.mass)

    def test_ship_must_only_unload_equipment_already_loaded(self):
        c = Container(1,1)
        p = Phaser(1,1)

        self.transport_ship.load(c)
        self.war_ship.load(p)

        equipments_length_before_unloading_ts = len(self.transport_ship.equipments)
        equipments_length_before_unloading_ws = len(self.war_ship.equipments)

        self.transport_ship.unload(c)
        self.war_ship.unload(p)
        self.assertGreater(equipments_length_before_unloading_ts, len(self.transport_ship.equipments))
        self.assertGreater(equipments_length_before_unloading_ws, len(self.war_ship.equipments))

    def test_equipment_unloaded_must_have_None_location(self):
        c = Container(1, 1)
        p = Phaser(1, 1)

        self.transport_ship.load(c)
        self.war_ship.load(p)

        self.transport_ship.unload(c)
        self.war_ship.unload(p)

        self.assertIsNone(c.location)
        self.assertIsNone(p.location)