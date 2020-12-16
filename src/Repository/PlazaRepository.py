import pickle
class PlazaRepositorio():
    def __init__(self, plazasDB=open("./pickleData/PlazasDB","rb")):
        self._plazasDB=pickle.load(plazasDB)

    @property
    def plazasDB(self):
        return self._plazasDB

    def buscarPorNumPlaza(self,numPlaza):
        print("Numero de la plaza en el buscar")
        print(self.plazasDB)
        print(numPlaza)
        stNum=str(numPlaza)
        return self.plazasDB[stNum]

    def agregarPlaza(self,dicPlaza):
        print("Plaza repositorio dic plaza:")
        pickle_in = open("./pickleData/PlazasDB","wb")
        pickle.dump(dicPlaza,pickle_in)
        pickle_in.close()
        print(dicPlaza)
    #Repasar los metodos de las plazas y la key que usa y no se guarda la plaza
