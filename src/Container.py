from src.Equipment import Equipment


class Container(Equipment):
    _nb_instances = 0

    def __init__(self, volume, mass):
        Equipment.__init__(self, volume, mass)
        self._nb_instances += 1
        self._name = "C-" + str(self._nb_instances)
