import pickle
class VehiculoRepositorio():
    def __init__(self,vehiculosDB= open("./pickleData/VehiculosDB",'rb')):
        self._vehiculosDB=vehiculosDB

    @property
    def vehiculosDB(self):
        return self._vehiculosDB

    def buscarPorMatricula(self,matricula):
        datos=pickle.load(self.vehiculosDB)
        try:
            return datos[str(matricula)]
        except:
            return None

    def agregarVehiculo(self,dictVehiculo):
        self.vehiculosDB.close()
        pickle_in=open("./pickleData/VehiculosDB","wb")
        pickle.dump(dictVehiculo,pickle_in)
        pickle_in.close()
        self._vehiculosDB = open("./pickleData/VehiculosDB",'rb')

