import pickle
class AdminRepositorio():
    def __init__(self,adminDB=open("./pickleData/AdminDB", "rb")):
        self._adminDB=adminDB

    @property
    def adminDB(self):
        return self._adminDB

    def buscarPorClave(self,clave):
        try:
            try:
                datos=pickle.load(self._adminDB)
                return datos[str(clave)]
            except EOFError:
                datos = pickle.load(open("./pickleData/AdminDB", "rb"))
                return datos[str(clave)]
        except KeyError:
            return None
