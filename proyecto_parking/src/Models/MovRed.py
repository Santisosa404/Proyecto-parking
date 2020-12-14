from proyecto_parking.src.Models.Vehiculo import Vehiculo
class MovRed(Vehiculo):
    def __init__(self,matricula,fechaLlegada=None,fechaSalida=None,Plaza=None):
        super().__init__(matricula,fechaLlegada,fechaSalida,Plaza)

