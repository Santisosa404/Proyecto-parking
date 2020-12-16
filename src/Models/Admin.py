class Admin():
    def __init__(self,nombre,clave):
        self._nombre=nombre
        self._clave=clave

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    @property
    def clave(self):
        return  self._clave
    @clave.setter
    def clave(self,clave):
        self._clave=clave

