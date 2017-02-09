import unittest

from src.Equipment import Equipment


class EquipmentTest(unittest.TestCase):
    def setUp(self):
        self.equipment = Equipment(10, 20)
        self.equipment2 = Equipment(100, 200)

    def tearDown(self):
        self.equipment = None
        self.equipment2 = None

    def test_equipment_constructor(self):
        self.assertIsNone(self.equipment.getName())
        self.assertEqual(self.equipment.getVolume(), 10)
        self.assertEqual(self.equipment.getMass(), 20)
        self.assertIsNone(self.equipment.getLocation())

        self.assertIsNone(self.equipment2.getName())
        self.assertEqual(self.equipment2.getVolume(), 100)
        self.assertEqual(self.equipment2.getMass(), 200)
        self.assertIsNone(self.equipment2.getLocation())