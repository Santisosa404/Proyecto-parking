from src.Models.Motocicleta import Motocicleta
from src.Models.MovRed import MovRed
from src.Models.Plaza import Plaza
from src.Models.Turismo import Turismo
from src.Service.PlazaService import PlazaService
import random
from datetime import  datetime

class ParkingController():

    def __init__(self,parkingService,vehiculoService,plazaService,ticketService):
        self._parkingService=parkingService
        self._vehiculoService=vehiculoService
        self._plazaService=plazaService
        self._ticketService=ticketService

    @property
    def parkingService(self):
        return self._parkingService
    @parkingService.setter
    def parkingService(self,parkingService):
        self._parkingService=parkingService
    @property
    def vehiculoService(self):
        return self._vehiculoService
    @vehiculoService.setter
    def vehiculoService(self,vehiculoService):
        self._vehiculoService=vehiculoService
    @property
    def plazaService(self):
        return self._plazaService
    @plazaService.setter
    def plazaService(self,plazaService):
        self._plazaService=plazaService
    @property
    def ticketService(self):
        return self._ticketService
    @ticketService.setter
    def ticketService(self,ticketService):
        self._ticketService=ticketService

    def estadoParking(self):
        p=self.parkingService.parking
        self.parkingService.actualizar()
        return  f'Quedan {p.plazasTotales-p.plazasActuales} plazas.\n' \
                f'{p.plazasTurismo} plazas para Turismos.\n' \
                f'{p.plazasMotocicletas} plazas para motocicletas.\n' \
                f'{p.plazasMovRed} plazas para Movilidad Reducida.'

    def depositarVehiculo(self,Vehiculo):
        if self.asignarPlaza(Vehiculo):
            self.ticketService.generarTicket(Vehiculo)
            self.vehiculoService.agregarVehiculo(Vehiculo)
            return print('El vehiculo ha sido depositado correctamente\n')
        else:
            return print('El vehiculo no se ha podido depositar\n')

    def asignarPlaza(self,Vehiculo):
        parking=self.parkingService.parking
        self.parkingService.actualizar()
        if parking.plazasActuales < parking.plazasTotales:
            if type(Vehiculo)== Turismo:
                plaza = Plaza(round((random.random()*parking.plazasTurismo+1-1)),Vehiculo,round(random.randrange(100000,600000)),True)
                plaza.Vehiculo=Vehiculo
                Vehiculo.Plaza=plaza
                Vehiculo.fechaLlegada= datetime.now()
                self.plazaService.agregarPlaza(plaza)
                return True
            elif type(Vehiculo) == MovRed:
                plaza = Plaza(round((random.random()*parking.plazasTurismo+1-1)),Vehiculo,round(random.randrange(100000,600000)),True)
                plaza.Vehiculo=Vehiculo
                Vehiculo.Plaza=plaza
                Vehiculo.fechaLlegada= datetime.now()
                self.plazaService.agregarPlaza(plaza)
                return True
            elif type(Vehiculo) == Motocicleta:
                plaza = Plaza(round((random.random()*parking.plazasTurismo+1-1)),Vehiculo,round(random.randrange(100000,600000)),True)
                plaza.Vehiculo=Vehiculo
                Vehiculo.Plaza=plaza
                Vehiculo.fechaLlegada= datetime.now()
                self.plazaService.agregarPlaza(plaza)
                return True
        else:
            return False
    # Matricula numPlaza Pin
    #Busco por matricula el coche y compruebo que el coche es el mismo que le que tiene la plaza y que el pin es el correcto
    def retirarVehiculo(self,matricula,numPlaza,pin):
        vehiculo =self.vehiculoService.buscarPorMatricula(matricula)
        plaza = self.plazaService.buscarPorPlazaVerificandoPin(pin,numPlaza)
        print("Datos del vehiculo")
        print(vehiculo.matricula)
        print("Pin de la plaza que tiene el vehiculo buscado")
        print(vehiculo.Plaza.pin)
        if plaza.__eq__(vehiculo.Plaza):
            vehiculo.fechaSalida=datetime.now()
            vehiculo.Plaza=None
            print("Impro dentro del if la plaza del vehiculo")
            print(plaza.Vehiculo)
            plaza.Vehiculo=None
            plaza.ocupada=False
            print("Casi termino")
            return self.ticketService.generarTicketSalida(vehiculo)
        else:
            return None

