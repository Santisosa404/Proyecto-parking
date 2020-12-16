
import locale
locale.setlocale(locale.LC_ALL, 'es-ES')
class Parking():
    def __init__(self,dicVehiculos,plazasTotales):
        self._dicVehiculos=dicVehiculos
        self._plazasTotales=plazasTotales
        self._plazasActuales= len(dicVehiculos.keys())
        self._plazasTurismo= round((self.plazasTotales*70)/100)
        self._plazasMotocicletas= round((self.plazasTotales*15)/100)
        self._plazasMovRed= round((self.plazasTotales*15)/100)
    @property
    def dicVehiculos(self):
        return self._dicVehiculos
    @dicVehiculos.setter
    def dicVehiculos(self,dicVehiculos):
        self._dicVehiculos=dicVehiculos
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
