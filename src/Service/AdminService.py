class AdminServicio():
    def __init__(self,adminRepositorio,dicAdmin):
        self._adminRepositorio=adminRepositorio
        self._dicAdmin=dicAdmin

    @property
    def adminRepositorio(self):
        return self._adminRepositorio
    @property
    def dicAdmin(self):
        return self._dicAdmin

    def comprobarClave(self,nombre,clave):
        admin=self.adminRepositorio.buscarPorClave(clave)

        if  admin != None and admin.nombre == nombre:
            return True
        else:
            return False
    def buscarPorClave(self,clave):
        return self.adminRepositorio.buscarPorClave(clave)
