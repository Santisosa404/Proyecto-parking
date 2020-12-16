class PlazaService():
    def __init__(self,plazaRepositorio,dicPlazas):
        self._plazaRepositorio=plazaRepositorio
        self._dicPlazas=dicPlazas

    @property
    def plazaRepositorio(self):
        return self._plazaRepositorio
    @property
    def dicPlazas(self):
        return self._dicPlazas


    def buscarPorPlazaVerificandoPin(self,pin,numPlaza):
        plaza= self.plazaRepositorio.buscarPorNumPlaza(numPlaza)
        print("Pin plaza buscada en plaza service")
        print(plaza.pin)
        print(type(plaza.pin))
        print("Pin pasado por atributo")
        print(pin)
        print(type(pin))
        if plaza.pin == pin:
            return plaza
        else:
            return None

    def agregarPlaza(self,plaza):
        strNum=str(plaza.numPlaza)
        self.dicPlazas[strNum]=plaza
        return self.plazaRepositorio.agregarPlaza(self.dicPlazas)
