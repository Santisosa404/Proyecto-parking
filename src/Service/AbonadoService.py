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
        try:
            abonado =self.abonadoRepositorio.buscarAbonadoDni(dni)
            if abonado.Vehiculo.matricula == matricula:
                return True
            else:
                return False
        except KeyError:
            return False
    def buscarPorDni(self,dni):
        return self.abonadoRepositorio.buscarAbonadoDni(dni)

    def buscarAbonados(self):
        return self.abonadoRepositorio.buscarAbonados()

    def agregarAbonado(self,nuevoAbonado):
        self.dicAbonado[nuevoAbonado.dni]=nuevoAbonado
        return self.abonadoRepositorio.agregarAbonado(self.dicAbonado)

    def editarAbonado(self,abonadoMod,dniOld):
        self.dicAbonado[abonadoMod.dni]=self.dicAbonado.pop(dniOld)
        self.abonadoRepositorio.agregarAbonado(self.dicAbonado)

    def eliminarAbonado(self,abonadoBorrar):
        self.dicAbonado.pop(abonadoBorrar.dni)
        self.abonadoRepositorio.agregarAbonado(self.dicAbonado)

    def imprimirPorMes(self,mes):
        resultado = self.abonadoRepositorio.buscarCancelacionPorMes(mes)
        print('Imprimiendo resultados')
        for i in resultado:
            print(i)

    def imprimirDiezDias(self):
        resultado = self.abonadoRepositorio.buscarCancelacionDiezDias()
        print('Imprimiendo resultados')
        for i in resultado:
            print(i)
