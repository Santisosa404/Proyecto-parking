import pickle

class VehiculoRepositorio():
    def __init__(self,vehiculosDB= open("./pickleData/VehiculosDB",'rb')):
        self._vehiculosDB=pickle.load(vehiculosDB)

    @property
    def vehiculosDB(self):
        return self._vehiculosDB

    def buscarPorMatricula(self,matricula):
        try:
            return self.vehiculosDB[matricula]
        except:
            return None

    def agregarVehiculo(self,dictVehiculo):
        pickle_in=open("./pickleData/VehiculosDB","wb")
        pickle.dump(dictVehiculo,pickle_in)
        pickle_in.close()

