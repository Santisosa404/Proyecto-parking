import pickle
class AdminRepositorio():
    def __init__(self,adminDB=open("./pickleData/AdminDB","rb")):
        self._adminDB=adminDB

    @property
    def adminDB(self):
        return self._adminDB

    def buscarPorClave(self,clave):
        datos=pickle.load(self.adminDB)
        return datos[str(clave)]
