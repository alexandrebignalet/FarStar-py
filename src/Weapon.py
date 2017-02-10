from abc import abstractmethod, ABCMeta

from src.Equipment import Equipment


class Weapon(Equipment):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, volume, mass):
        super(Weapon, self).__init__(volume, mass)
        self._equipped = False

    @property
    def equipped(self):
        return self._equipped

    @equipped.setter
    def equipped(self, equipped):
        self._equipped = equipped