import unittest

from src.Blaster import Blaster
from src.Container import Container
from src.TransportShip import TransportShip


class TransportShipTest(unittest.TestCase):

    def setUp(self):
        self.transport_ship = TransportShip(100, 200, 90, 200)

    def tearDown(self):
        self.transport_ship = None

    def test_constructor(self):
        self.assertEqual(self.transport_ship.volume_capacity, 90)
        self.assertEqual(self.transport_ship.weight_capacity, 200)

    def test_location_setter_overriding(self):
        with self.assertRaises(ValueError):
            w = Blaster(1,1,3)
            try:
                self.transport_ship.location = w
            except ValueError as e:
                self.assertEquals(e.args, ('A Ship can only be located in a TransportShip',))
                raise

    def test_must_raise_if_volume_capacity_gt_volume(self):
        with self.assertRaises(AssertionError):
            self.assertRaises(AssertionError, TransportShip(10,20,30,40))

    def test_load_equipments_list_must_contain_equipment_in_arg(self):
        c = Container(1,1)
        c2 = Container(1,1)

        self.transport_ship.load(c)
        self.transport_ship.load(c2)

        self.assertEqual(self.transport_ship.equipments.index(c), 0)
        self.assertEqual(self.transport_ship.equipments.index(c2), 1)

    def test_load_must_raise_if_volume_capacity_exceed(self):
        with self.assertRaises(AssertionError):
            c = Container(1000,1000)
            self.assertRaises(AssertionError, self.transport_ship.load(c))

    def test_load_must_raise_if_weight_capacity_exceed(self):
        with self.assertRaises(AssertionError):
            c = Container(10,1000)

            self.assertRaises(AssertionError, self.transport_ship.load(c))

    def test_load_must_raise_if_arg_is_not_an_equipment_object(self):
        with self.assertRaises(AssertionError):
            arg = 10
            self.assertRaises(AssertionError, self.transport_ship.load(arg))

    def test_load_must_raise_if_equipment_arg_is_loaded_elsewhere(self):
        with self.assertRaises(AssertionError):
            t = TransportShip(10,20,9,12)
            c = Container(1,1)
            t.load(c)

            self.assertRaises(AssertionError, self.transport_ship.load(c))

    def test_volume_and_weight_capacity_remaining_must_decrease_after_equipment_loading(self):
        base_volume_capacity = self.transport_ship.volume_capacity
        base_weight_capacity = self.transport_ship.weight_capacity

        c = Container(1,1)

        self.transport_ship.load(c)

        self.assertLess(self.transport_ship.volume_capacity_remaining, base_volume_capacity)
        self.assertLess(self.transport_ship.weight_capacity_remaining, base_weight_capacity)

    def test_equipment_location_must_be_set_to_the_current_loader_after_loading(self):
        c = Container(1,1)

        self.assertIsNone(c.location)

        self.transport_ship.load(c)

        self.assertEqual(self.transport_ship, c.location)

    def test_ship_weight_and_volume_capacity_remaining_must_increase_after_unloading(self):
        c = Container(1,1)
        self.transport_ship.load(c)
        weight_capacity_remaining_before_unloading = self.transport_ship.weight_capacity_remaining
        volume_capacity_remaining_before_unloading = self.transport_ship.volume_capacity_remaining

        self.transport_ship.unload(c)

        self.assertGreater(self.transport_ship.weight_capacity_remaining, weight_capacity_remaining_before_unloading)
        self.assertGreater(self.transport_ship.volume_capacity_remaining, volume_capacity_remaining_before_unloading)

