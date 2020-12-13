class Abonado():
    def __init__(self,nombre,apellidos,dni,Vehiculo,Plaza,numTarjeta,tipoAbono,email,fechaActivacion,fechaCancelacion):
        self._nombre=nombre
        self._apellidos=apellidos
        self._dni=dni
        self._Vehiculo=Vehiculo
        self._Plaza=Plaza
        self._numTarjeta=numTarjeta
        self._tipoAbono=tipoAbono
        self._email=email
        self._fechaActivacion=fechaActivacion
        self._fechaCancelacion=fechaCancelacion

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    @property
    def apellidos(self):
        return self._apellidos
    @apellidos.setter
    def apellidos(self,apellidos):
        self._apellidos=apellidos
    @property
    def dni(self):
        return self._dni
    @dni.setter
    def dni(self,dni):
        self._dni=dni
    @property
    def Vehiculo(self):
        return self._Vehiculo
    @Vehiculo.setter
    def Vehiculo(self,Vehiculo):
        self._Vehiculo=Vehiculo
    @property
    def Plaza(self):
        return self._Plaza
    @Plaza.setter
    def Plaza(self,Plaza):
        self._Plaza=Plaza
    @property
    def numTarjeta(self):
        return self._numTarjeta
    @numTarjeta.setter
    def numTarjeta(self,numTarjeta):
        self._numTarjeta=numTarjeta
    @property
    def tipoAbono(self):
        return self._tipoAbono
    @tipoAbono.setter
    def tipoAbono(self,tipoAbono):
        self._tipoAbono=tipoAbono
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email):
        self._email=email
    @property
    def fechaActivacion(self):
        return self._fechaActivacion
    @fechaActivacion.setter
    def fechaActivacion(self,fechaActivacion):
        self._fechaActivacion=fechaActivacion
    @property
    def fechaCancelacion(self):
        return self._fechaActivacion
    @fechaActivacion.setter
    def fechaActivacion(self,fechaActivacion):
        self._fechaActivacion=fechaActivacion
