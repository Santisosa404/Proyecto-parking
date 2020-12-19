from datetime import datetime

from src.Models.Abonado import Abonado

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
        print("Imprimiendo Abonados")
        for i in dicAbonados.values():
            print(i)
    def darDeAlta(self,nombre,apellidos,dni,email,numTarjeta,VehiculoAbonado,PlazaAbonado,tipoAbono):
        hoy =datetime.now()
        if tipoAbono.lower()=='Mensual'.lower():
            hoy = hoy.replace(month=+1)
            nuevoAbonado = Abonado(nombre,apellidos,dni,VehiculoAbonado,PlazaAbonado,numTarjeta,tipoAbono,email,datetime.now(),datetime.now().replace(month=datetime.now().month+1))
            self.abonadoService.agregarAbonado(nuevoAbonado)
        elif tipoAbono.lower()== 'Trimestral'.lower():
            nuevoAbonado = Abonado(nombre,apellidos,dni,VehiculoAbonado,PlazaAbonado,numTarjeta,tipoAbono,email,datetime.now(),datetime.now().replace(month=datetime.now().month+3))
            self.abonadoService.agregarAbonado(nuevoAbonado)
        elif tipoAbono.lower() == 'Semestral'.lower():
            nuevoAbonado = Abonado(nombre,apellidos,dni,VehiculoAbonado,PlazaAbonado,numTarjeta,tipoAbono,email,datetime.now(),datetime.now().replace(month=datetime.now().month+7))
            self.abonadoService.agregarAbonado(nuevoAbonado)
        elif tipoAbono.lower() == 'Anual'.lower():
            nuevoAbonado = Abonado(nombre,apellidos,dni,VehiculoAbonado,PlazaAbonado,numTarjeta,tipoAbono,email,datetime.now(),datetime.now().replace(year=datetime.now().year+1))
            self.abonadoService.agregarAbonado(nuevoAbonado)
        return True

    def modificarAbonado(self,abonadoMod,nombre,apellidos,correo,dni,dniOld):
        abonadoMod.nombre = nombre
        abonadoMod.apellidos = apellidos
        abonadoMod.correo = correo
        abonadoMod.dni = dni
        self.abonadoService.editarAbonado(abonadoMod,dniOld)

    def renovarCancelacion(self,abonado):
        tipoAbono=abonado.tipoAbono
        if tipoAbono.lower()=='Mensual'.lower():
            abonado.fechaActivacion=datetime.now()
            abonado.fechaCancelacion=datetime.now().replace(month=datetime.now().month+1)
        elif tipoAbono.lower()== 'Trimestral'.lower():
            abonado.fechaActivacion=datetime.now()
            abonado.fechaCancelacion=datetime.now().replace(month=datetime.now().month+3)
        elif tipoAbono.lower() == 'Semestral'.lower():
            abonado.fechaActivacion=datetime.now()
            abonado.fechaCancelacion=datetime.now().replace(month=datetime.now().month+7)
        elif tipoAbono.lower() == 'Anual'.lower():
            abonado.fechaActivacion=datetime.now()
            abonado.fechaCancelacion=datetime.now().replace(year=datetime.now().year+1)

        self.abonadoService.editarAbonado(abonado,abonado.dni)

    def darDeBaja(self,abonadoBorrar):
        self.abonadoService.eliminarAbonado(abonadoBorrar)

    def imprimirConsulta(self,mes=None):
        if mes == None:
             self.abonadoService.imprimirDiezDias()
        else:
            self.abonadoService.imprimirPorMes(mes)
