from src.Equipment import Equipment


class Container(Equipment):
    _nb_instances = 0

    def __init__(self, volume, mass):
        super(Container, self).__init__(volume, mass)
        Container._nb_instances += 1
        self._name = "C-" + str(Container._nb_instances)
