class VehiculoService():
    def __init__(self,vehiculoRepositorio,dicVehiculo):
        self._VehiculoRepositorio = vehiculoRepositorio
        self._dicVehiculo=dicVehiculo
    @property
    def vehiculoRepositorio(self):
        return self._VehiculoRepositorio
    @property
    def dicVehiculo(self):
        return self._dicVehiculo

    def buscarPorMatricula(self,matricula):
       return self.vehiculoRepositorio.buscarPorMatricula(matricula)

    def agregarVehiculo(self,Vehiculo):
        self.dicVehiculo[Vehiculo.matricula] =Vehiculo
        return self.vehiculoRepositorio.agregarVehiculo(self.dicVehiculo)
