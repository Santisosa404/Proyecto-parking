from src.Models.Vehiculo import Vehiculo

class Turismo(Vehiculo):
    def __init__(self,matricula,fechaLlegada=None,fechaSalida=None,Plaza=None):
        super().__init__(matricula,fechaLlegada,fechaSalida,Plaza)
