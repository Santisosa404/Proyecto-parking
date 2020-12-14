from proyecto_parking.src.Models import MovRed
from proyecto_parking.src.Models.Motocicleta import Motocicleta
from proyecto_parking.src.Models.Turismo import Turismo
import locale
locale.setlocale(locale.LC_ALL, 'es-ES')
class Parking():
    def __init__(self,listaVehiculos,plazasTotales):
        self._listaVehiculos=listaVehiculos
        self._plazasTotales=plazasTotales
        self._plazasActuales= len(listaVehiculos)
        self._plazasTurismo= round((self.plazasTotales*70)/100)
        self._plazasMotocicletas= round((self.plazasTotales*15)/100)
        self._plazasMovRed= round((self.plazasTotales*15)/100)
    @property
    def listaVehiculos(self):
        return self._listaVehiculos
    @listaVehiculos.setter
    def listaVehiculos(self,listaVehiculos):
        self._listaVehiculos=listaVehiculos
    @property
    def plazasTotales(self):
        return self._plazasTotales
    @plazasTotales.setter
    def plazasTotales(self,plazasTotales):
        self._plazasTotales=plazasTotales
    @property
    def plazasTurismo(self):
        return self._plazasTurismo
    @plazasTurismo.setter
    def plazasTurismo(self,plazasTurismo):
        self._plazasTurismo=plazasTurismo
    @property
    def plazasMotocicletas(self):
        return self._plazasMotocicletas
    @plazasMotocicletas.setter
    def plazasMotocicletas(self,plazasMotocicletas):
        self._plazasMotocicletas=plazasMotocicletas
    @property
    def plazasMovRed(self):
        return self._plazasMovRed
    @plazasMovRed.setter
    def plazasMovRed(self,plazasMovRed):
        self._plazasMovRed = plazasMovRed
    @property
    def plazasActuales(self):
        return self._plazasActuales
    @plazasActuales.setter
    def plazasActuales(self,plazasActuales):
        self._plazasActuales=plazasActuales

    def __str__(self):
            return f'El parking tiene {self._plazasTotales} plazas totales de las cuales:\n' \
               f'{self._plazasTurismo} plazas son para turismos.\n{self._plazasMotocicletas} plazas son para Motocicletas.\n{self._plazasMovRed} plazas son para Movilidad Reducida'

    def generarTicket(self,Vehiculo):
        print("********** Impriminedo Ticket **********\n\n")
        print(f'El vehiculo con matricula ${Vehiculo.matricula}\n'
              f'Ingresó el {Vehiculo.fechaLlegada.strftime("%A %d %B %Y %I:%M")} en la plaza {Vehiculo.Plaza.numPlaza}\n'
              f'Su pin de recogida es: {Vehiculo.Plaza.pin}\nTenga un buen dia\n')

    def actualizar(self):
        turismo,moto,mov = 0,0,0
        for i in self.listaVehiculos:
            if type(i) == Turismo:
                turismo +=1
            elif type(i) == Motocicleta:
                moto +=1
            elif type(i) == MovRed:
                mov+=1
        self._plazasActuales = len(self.listaVehiculos)
        self._plazasTurismo -=turismo
        self._plazasMotocicletas -=moto
        self._plazasMovRed -=mov
