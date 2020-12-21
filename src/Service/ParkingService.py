from src.Models.MovRed import MovRed
from src.Models.Motocicleta import Motocicleta
from src.Models.Turismo import Turismo

class Parkingservice():
    def __init__(self,parking=None):
        self._parking=parking

    @property
    def parking(self):
        return self._parking
    @parking.setter
    def parking(self,parking):
        self._parking=parking


    def actualizar(self):
        turismo,moto,mov = 0,0,0
        for i in self.parking.dicVehiculos.values():
            if type(i) == Turismo:
                turismo += 1
            elif type(i) == Motocicleta:
                moto += 1
            elif type(i) == MovRed:
                mov += 1
        self.parking.plazasActuales = self.parking.plazasTotales-len(self.parking.dicVehiculos.keys())
        self.parking.plazasTurismo -= turismo
        self.parking.plazasMotocicletas -= moto
        self.parking.plazasMovRed -= mov
