from abc import ABCMeta, abstractmethod

from src.Equipment import Equipment


class Ship(Equipment):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, volume, mass):
        Equipment.__init__(self, volume, mass)
        self._equipments = []

    @property
    def equipments(self):
        return self._equipments

    @property
    def mass(self):
        total = self._mass

        for equipment in self.equipments:
            total += equipment.mass

        return total

    @abstractmethod
    def load(self, equipment):pass

    def unload(self, equipment):
        try:
            self._equipments.remove(equipment)
        except ValueError as e:
            raise e
        equipment.location = None

    @Equipment.location.setter
    def location(self, ship):
        from src.TransportShip import TransportShip

        if not isinstance(ship, TransportShip) and ship is not None:
            raise ValueError('A Ship can only be located in a TransportShip')

        self._location = ship

