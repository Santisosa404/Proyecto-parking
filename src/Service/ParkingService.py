from src.Models import MovRed
from src.Models.Motocicleta import Motocicleta
from src.Models.Ticket import Ticket
from src.Models.Turismo import Turismo

class Parkingservice():
    def __init__(self,parking):
        self._parking=parking

    @property
    def parking(self):
        return self._parking
    @parking.setter
    def parking(self,parking):
        self._parking=parking

    def generarPago(self,Vehiculo):
        if type(Vehiculo) == Turismo:
            return (Vehiculo.fechaLlegada.minute-Vehiculo.fechaSalida.minute)*0.12
        elif type(Vehiculo) == Motocicleta:
            return (Vehiculo.fechaLlegada.minute-Vehiculo.fechaSalida.minute)*0.08
        elif type(Vehiculo) == MovRed:
            return (Vehiculo.fechaLlegada.minute-Vehiculo.fechaSalida.minute)*0.10

    def actualizar(self):
        turismo,moto,mov = 0,0,0
        for i in self.parking.dicVehiculos.values():
            if type(i) == Turismo:
                turismo +=1
            elif type(i) == Motocicleta:
                moto +=1
            elif type(i) == MovRed:
                mov+=1
        self.parking.plazasActuales = self.parking.plazasTotales-len(self.parking.dicVehiculos.keys())
        self.parking.plazasTurismo -=turismo
        self.parking.plazasMotocicletas -=moto
        self.parking.plazasMovRed -=mov