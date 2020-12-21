from src.Models.Motocicleta import Motocicleta
from src.Models.MovRed import MovRed
from src.Models.Plaza import Plaza
from src.Models.Turismo import Turismo
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
        return  f'Quedan {p.plazasActuales} plazas.\n' \
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

    def depositarVehiculoAbonado(self,Abonado,pin):
        if int(Abonado.Plaza.pin) == int(pin):
            Abonado.Plaza.ocupada=True
            Abonado.Vehiculo.Plaza=Abonado.Plaza
            Abonado.Vehiculo.fechaLlegada=datetime.now()
            return print(f"El vehiculo ha sido depositado correctamente.\nTenga un buen dia {Abonado.nombre}")
        else:
            print("Credenciales incorrectas")
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
    def retirarVehiculo(self,matricula,numPlaza,pin):
        try:
            vehiculo =self.vehiculoService.buscarPorMatricula(matricula)
            plaza = self.plazaService.buscarPorPlazaVerificandoPin(pin,numPlaza)
            print(vehiculo.Plaza.pin)
            if plaza.__eq__(vehiculo.Plaza):
                vehiculo.fechaSalida=datetime.now()
                vehiculo.Plaza=None
                plaza.Vehiculo=None
                plaza.ocupada=False
                return self.ticketService.generarTicketSalida(vehiculo)
            else:
                return None
        except KeyError:
            print("No se ha podido encontrar el vehiculo especificado")
    def retirarVehiculoAbonado(self,Abonado):
        Abonado.Vehiculo.Plaza =None
        Abonado.Vehiculo.fechaSalida=datetime.now()
        return print("El vehiculo ha sido retirado correctamente")
