import pickle
class AbonadoRepositorio():
    def __init__(self,abonadosDB=open("./pickleData/AbonadosDB","rb")):
        self._abonadosDB=abonadosDB

    @property
    def abonadosDB(self):
        return self._abonadosDB

    def buscarAbonadoDni(self,dni):
        try:
            datos =pickle.load(self.abonadosDB)
        except EOFError:
            datos=pickle.load(open("./pickleData/AbonadosDB","rb"))
        return datos[dni]

    def buscarAbonados(self):
        datos=pickle.load(self.abonadosDB)
        return datos
