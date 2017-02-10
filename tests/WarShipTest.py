import unittest

from src.Blaster import Blaster
from src.Container import Container
from src.Phaser import Phaser
from src.TransportShip import TransportShip
from src.WarShip import WarShip


class WarShipTest(unittest.TestCase):

    def setUp(self):
        self.war_ship = WarShip(100, 200, 2)

    def tearDown(self):
        self.war_ship = None

    def test_constructor(self):
        self.assertEqual(self.war_ship.max_nb_weapons, 2)

    def test_must_raise_if_max_nb_weapons_equipped_exceeded(self):
        with self.assertRaises(AssertionError):
            b = Blaster(1, 1, 45)
            p = Phaser(1,1)

            self.war_ship.load(b)
            self.war_ship.load(p)

            p2 = Phaser(2,2)

            self.assertRaises(AssertionError, self.war_ship.load(p2))

    def test_load_anything_else_than_a_weapon_must_raise(self):
        with self.assertRaises(AssertionError):
            c = Container(1,1)
            ts = TransportShip(13, 24, 12, 45)

            self.assertRaises(AssertionError, self.war_ship.load(c))


    def test_load_equipments_list_must_contain_weapon_arg_after_loading(self):
        p = Phaser(1, 1)
        p2 = Phaser(1, 1)

        self.war_ship.load(p)
        self.war_ship.load(p2)

        self.assertEqual(self.war_ship.equipments.index(p), 0)
        self.assertEqual(self.war_ship.equipments.index(p2), 1)

    def test_load_must_raise_if_arg_is_not_a_weapon_object(self):
        with self.assertRaises(AssertionError):
            arg = 10
            self.assertRaises(AssertionError, self.war_ship.load(arg))

    def test_load_must_raise_if_weapon_arg_is_loaded_elsewhere(self):
        with self.assertRaises(AssertionError):

            t = TransportShip(10,20,9,12)
            p = Phaser(1,1)
            t.load(p)

            self.assertRaises(AssertionError, self.war_ship.load(p))

    def test_equipment_location_must_be_set_to_the_current_loader_after_loading(self):
        p = Phaser(1,1)

        self.assertIsNone(p.location)

        self.war_ship.load(p)

        self.assertEqual(self.war_ship, p.location)

