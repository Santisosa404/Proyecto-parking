from proyecto_parking.src.Controller.ParkingController import ParkingController
from proyecto_parking.src.Models.MovRed import MovRed
from proyecto_parking.src.Models.Motocicleta import Motocicleta
from proyecto_parking.src.Models.Parking import Parking
from proyecto_parking.src.Models.Plaza import Plaza
from proyecto_parking.src.Models.Turismo import Turismo
import pickle
plazasParking=int(input("Antes de comenzar, debo saber de cuantas plazas será el parking\n"))

v1 = Turismo('2323')
pla1 = Plaza(77,v1,1234,True)
v1.Plaza=pla1

dictTicket = {}
listaVehiculos =[v1]

with open('./pickleData/listaVehiculos.txt','wb') as VehiculosPickle:
    pickle.dump(listaVehiculos,VehiculosPickle)

p1 = Parking(listaVehiculos,plazasParking)
parkingController = ParkingController(p1)
op=-1
while op!='0':
    print('Bienvendio al parking Bustillo 2.0.\n'
          'Pulse 1 para hacer uso del parking sin abono\n'
          'Pulse 2 para hacer uso del parking con abono\n'
          'Pulse 3 para acceder a la administracion del parking')
    op=input()
    if op =='1':
        op1=-1
        while op1 !='0':
            print(parkingController.estadoParking())
            print("Pulse 1 para depositar el vehiculo\n"
                  "Pulse 2 para retirar el vehiculo")
            op1= input()
            if op1 =='1':
                if p1.plazasActuales !=p1.plazasTotales:
                    tipo=input('¿Qué vehiculo va a depositar?\n')
                    matricula=input('Matricula del vehiculo a ingresar\n')
                    if tipo.lower() == 'turismo':
                        vehiculo=Turismo(matricula)
                    elif tipo.lower() == 'motocicleta':
                        vehiculo=Motocicleta(matricula)
                    elif tipo.lower() == 'movilidad reducida':
                        vehiculo=MovRed(matricula)
                    parkingController.depositarVehiculo(vehiculo)
                else:
                    print("El parking está lleno, no es posible depositar un vehiculo")
            elif op1 == '2':
                print("")
    elif op=='2':
        print("Pulse 1 para depositar su vehiculo\n"
              "Pulse 2 para retirar su vehiculo")
    elif op=='3':
        print('F')

