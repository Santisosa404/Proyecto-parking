from src.Models.Motocicleta import Motocicleta
from src.Models.Plaza import Plaza
from src.Models.Turismo import Turismo
from src.Service.PlazaService import PlazaService
import random
from datetime import  datetime

class ParkingController():

    def __init__(self,Parking):
        self._Parking=Parking

    @property
    def Parking(self):
        return self._Parking
    @Parking.setter
    def Parking(self,Parking):
        self._Parking=Parking

    def estadoParking(self):
        self.Parking.actualizar()
        return  f'Quedan {self.Parking.plazasTotales-self.Parking.plazasActuales} plazas.\n' \
                f'{self.Parking.plazasTurismo} plazas para Turismos.\n' \
                f'{self.Parking.plazasMotocicletas} plazas para motocicletas.\n' \
                f'{self.Parking.plazasMovRed} plazas para Movilidad Reducida.'

    def depositarVehiculo(self,Vehiculo):
        if self.asignarPlaza(Vehiculo):
            self.Parking.generarTicket(Vehiculo)
            return print('El vehiculo ha sido depositado correctamente\n')
        else:
            return print('El vehiculo no se ha podido depositar\n')

    def asignarPlaza(self,Vehiculo):
        if type(Vehiculo)== Turismo:
            plaza = Plaza(round((random.random()*self.Parking.plazasTurismo+1-1)),Vehiculo,round(random.randrange(100000,600000)),True)
            Vehiculo.Plaza=plaza
            Vehiculo.fechaLlegada= datetime.now()
            return True
        elif type(Vehiculo) == Motocicleta:
            plaza = Plaza(round((random.random()*self.Parking.plazasTurismo+1-1)),Vehiculo,round(random.randrange(100000,600000)),True)
            Vehiculo.Plaza=plaza
            Vehiculo.fechaLlegada= datetime.now()
            return True
        elif type(Vehiculo) == Motocicleta:
            plaza = Plaza(round((random.random()*self.Parking.plazasTurismo+1-1)),Vehiculo,round(random.randrange(100000,600000)),True)
            Vehiculo.Plaza=plaza
            Vehiculo.fechaLlegada= datetime.now()
            return True

