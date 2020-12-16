class AbonadoServicio():
    def __init__(self,abonadoRepositorio,dicAbonado):
        self._abonadoRepositorio=abonadoRepositorio
        self._dicAbonado=dicAbonado

    @property
    def abonadoRepositorio(self):
        return self._abonadoRepositorio
    @property
    def dicAbonado(self):
        return self._dicAbonado

    def comprobarAbonado(self,dni,matricula):
        abonado =self.abonadoRepositorio.buscarAbonadoDni(dni)
        if abonado.Vehiculo.matricula == matricula:
            return abonado
        else:
            return None

    def buscarPorDni(self,dni):
        return self.abonadoRepositorio.buscarAbonadoDni(dni)