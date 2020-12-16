import pickle
class PlazaRepositorio():
    def __init__(self, plazasDB=open("./pickleData/PlazasDB","rb")):
        self._plazasDB=plazasDB

    @property
    def plazasDB(self):
        return self._plazasDB

    def buscarPorNumPlaza(self,numPlaza):
        datos = pickle.load(self.plazasDB)
        print("Numero de la plaza en el buscar datos")
        print(datos)
        print(numPlaza)
        stNum=str(numPlaza)
        return datos[stNum]

    def agregarPlaza(self,dicPlaza):
        print("Plaza repositorio dic plaza:")
        pickle_in = open("./pickleData/PlazasDB","wb")
        pickle.dump(dicPlaza,pickle_in)
        pickle_in.close()
        print(dicPlaza)
    #Repasar los metodos de las plazas y la key que usa y no se guarda la plaza
