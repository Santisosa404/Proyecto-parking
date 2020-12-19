import pickle
from datetime import datetime


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
        try:
            datos =pickle.load(self.abonadosDB)
        except EOFError:
            datos=pickle.load(open("./pickleData/AbonadosDB","wb"))
        return datos

    def agregarAbonado(self,dicAbonados):
        self.abonadosDB.close()
        pickle_in = open("./pickleData/AbonadosDB","wb")
        pickle.dump(dicAbonados,pickle_in)
        pickle_in.close()
        self._abonadosDB = open("./pickleData/AbonadosDB","rb")

    def buscarCancelacionDiezDias(self):
        datos = pickle.load(self.abonadosDB)
        resultado=list()
        for i in datos.values():
            if i.fechaCancelacion == datetime.now().replace(day=datetime.now().day+10):
                resultado.append(i)
        return resultado

    def buscarCancelacionPorMes(self,mes):
        resultado=list()
        try:
            datos = pickle.load(self.abonadosDB)

        except EOFError:
            datos = pickle.load(open("./pickleData/AbonadosDB","rb"))
        for i in datos.values():
            if i.fechaCancelacion.month == mes:
                resultado.append(i)
        return resultado
