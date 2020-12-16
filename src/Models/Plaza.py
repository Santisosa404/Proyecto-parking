class Plaza():
    def __init__(self,numPlaza,Vehiculo,pin,ocupada):
        self._numPlaza=numPlaza
        self._Vehiculo=Vehiculo
        self._pin=pin
        self._ocupada=ocupada

    @property
    def numPlaza(self):
        return self._numPlaza
    @numPlaza.setter
    def numPlaza(self,numPlaza):
        self._numPlaza=numPlaza
    @property
    def Vehiculo(self):
        return self._Vehiculo
    @Vehiculo.setter
    def Vehiculo(self,Vehiculo):
        self._Vehiculo=Vehiculo
    @property
    def pin(self):
        return self._pin
    @pin.setter
    def pin(self,pin):
        self._pin=pin
    @property
    def ocupada(self):
        return self._ocupada
    @ocupada.setter
    def ocupada(self,ocupada):
        self._ocupada=ocupada

    def __eq__(self, other):
        return self.pin == other.pin
