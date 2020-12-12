class DomainCar:

    def __init__(self):
        self.name = None
        self.id = None

    @property
    def carName(self):
        return self.name

    @carName.setter
    def carName(self, value):
        self.name = value

    @carName.getter
    def carName(self):
        return self.name

    @property
    def carId(self):
        return self.id

    @carId.setter
    def carId(self, value):
        self.id = value

    @carId.getter
    def carId(self):
        return self._id

