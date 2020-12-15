class Ticket():
    def __init__(self,Vehiculo,pagado=False):
        self._Vehiculo=Vehiculo
        self._pagado=pagado

    @property
    def Vehiculo(self):
        return self._Vehiculo
    @Vehiculo.setter
    def Vehiculo(self,Vehiculo):
        self._Vehiculo=Vehiculo
    @property
    def pagado(self):
        return self._pagado
    @pagado.setter
    def pagado(self,pagado):
        self._pagado=pagado

    def __str__(self):
        if self.Vehiculo.fechaSalida ==None:
            return f'El vehiculo con matricula {self.Vehiculo.matricula}\n'\
                   f'Ingresó el {self.Vehiculo.fechaLlegada.strftime("%A %d %B %Y %I:%M")} en la plaza {self.Vehiculo.Plaza.numPlaza}\n' \
                   f'Para retirar el vehiculo será necesario el uso del pin {self.Vehiculo.Plaza.pin}'
        else:
            return f'El vehiculo con matricula {self.Vehiculo.matricula}\n'\
                   f'Ingresó el {self.Vehiculo.fechaLlegada.strftime("%A %d %B %Y %I:%M")} en la plaza {self.Vehiculo.Plaza.numPlaza}\n' \
                   f'La salida del vehiculo fue el {self.Vehiculo.fechaLlegada.strftime("%A %d %B %Y %I:%M")}\nEl coste total de estancia es de {self.generarPago(self.Vehiculo)} €\n'

