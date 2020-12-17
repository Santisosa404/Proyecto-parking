from datetime import datetime


class AdminControler():
    def __init__(self, ticketService,abonadoService):
        self._ticketService = ticketService
        self._abonadoService=abonadoService

    @property
    def ticketService(self):
        return self._ticketService

    @ticketService.setter
    def ticketService(self, ticketService):
        self._ticketService = ticketService
    @property
    def abonadoService(self):
        return self._abonadoService

    @abonadoService.setter
    def abonadoService(self, abonadoService):
        self._abonadoService = abonadoService

    def imprimirFacturacion(self, fecha1, fecha2):
        facturacion = self.ticketService.facturacionFechas(fecha1, fecha2)

        for i, j in facturacion.items():
            print(f'El vehiculo con matricula {i}, pasó {(j.Vehiculo.fechaSalida-j.Vehiculo.fechaLlegada)} minutos en el parking\n'
                f'El coste total de su estancia fue de {j.generarPago(j.Vehiculo)} €\n')

    def convertirFecha(self,fecha):
        day, month, end = map(str, fecha.split('-'))
        year, hora = end.split(' ')
        minute, second = map(int, hora.split(':'))
        return datetime(int(year), int(month), int(day), int(minute), int(second))

    def imprimirAbonados(self):
        dicAbonados=self.abonadoService.buscarAbonados()
        for i in dicAbonados.values():
            print(i)

