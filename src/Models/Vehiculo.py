class Vehiculo():
    def __init__(self,matricula,fechaLlegada=None,fechaSalida=None,Plaza=None):
        self._matricula=matricula
        self._fechaLlegada= fechaLlegada
        self._fechaSalida=fechaSalida
        self._Plaza = Plaza

    @property
    def matricula(self):
        return  self._matricula
    @matricula.setter
    def matricula(self,matricula):
        self._matricula=matricula
    @property
    def fechaLlegada(self):
        return self._fechaLlegada
    @fechaLlegada.setter
    def fechaLlegada(self,fechaLlegada):
        self._fechaLlegada=fechaLlegada
    @property
    def fechaSalida(self):
        return self._fechaSalida
    @fechaSalida.setter
    def fechaSalida(self,fechaSalida):
        self._fechaSalida=fechaSalida
    @property
    def Plaza(self):
        return self._Plaza
    @Plaza.setter
    def Plaza(self, Plaza):
        self._Plaza=Plaza

    
