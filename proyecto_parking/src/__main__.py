from src.Controller.ParkingController import ParkingController
from src.Models.MovRed import MovRed
from src.Models.Motocicleta import Motocicleta
from src.Models.Parking import Parking
from src.Models.Plaza import Plaza
from src.Models.Turismo import Turismo
import pickle


from src.Repository.PlazaRepository import PlazaRepositorio
from src.Repository.TicketRepository import TicketRepositorio
from src.Repository.VehiculoRepository import VehiculoRepositorio
from src.Service.ParkingService import Parkingservice
from src.Service.PlazaService import PlazaService
from src.Service.TicketService import TicketServicio
from src.Service.VehiculoService import VehiculoService

plazasParking=int(input("Antes de comenzar, debo saber de cuantas plazas será el parking\n"))




# pickle_in=open("./pickleData/VehiculosDB","rb")
# Vehiculos_in=pickle.load(pickle_in)
# print(Vehiculos_in[0].matricula)

v1 = Turismo('2323')
pla1 = Plaza(77,v1,1234,True)
v1.Plaza=pla1
pla1.Vehiculo=v1
dicVehiculos =dict()
dicVehiculos[v1.matricula]=v1

dicPlazas = dict()
dicPlazas['77'] = pla1
dicTicket = dict()

# pickle_ticket=open("./pickleData/TicketDB","wb")
# pickle.dump(dicTicket,pickle_ticket)
# pickle_ticket.close()

# pickle_Vehiculos=open("./pickleData/VehiculosDB","wb")
# pickle.dump(dicVehiculos,pickle_Vehiculos)
# pickle_Vehiculos.close()

pickle_Plazas = open("./pickleData/PlazasDB","wb")
pickle.dump(dicPlazas,pickle_Plazas)
pickle_Plazas.close()


p1 = Parking(dicVehiculos,plazasParking)
parkingServicio = Parkingservice(p1)

vehiculoRepositorio=VehiculoRepositorio()
vehiculoServicio = VehiculoService(vehiculoRepositorio,dicVehiculos)

plazaRepositorio=PlazaRepositorio()
plazaServicio=PlazaService(plazaRepositorio,dicPlazas)

ticketRepositorio=TicketRepositorio()
ticketServicio=TicketServicio(ticketRepositorio,dicTicket)

parkingController = ParkingController(parkingServicio,vehiculoServicio,plazaServicio,ticketServicio)
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
            print(p1)
            print("Pulse 1 para depositar el vehiculo\n"
                  "Pulse 2 para retirar el vehiculo")
            op1= input()
            if op1 =='1':
                tipo=input('¿Qué vehiculo va a depositar?\n')
                matricula=input('Matricula del vehiculo a ingresar\n')
                if tipo.lower() == 'turismo':
                    vehiculo=Turismo(matricula)
                elif tipo.lower() == 'motocicleta':
                    vehiculo=Motocicleta(matricula)
                elif tipo.lower() == 'movilidad reducida':
                    vehiculo=MovRed(matricula)
                parkingController.depositarVehiculo(vehiculo)
            elif op1 == '2':
                matricula=input("Para retirar el vehiculo será requerido:\n"
                                "Matricula del vehiculo:")
                numPlaza=input('Plaza asignada: ')
                pinPlaza=input('Pin asociado: ')
                parkingController.retirarVehiculo(matricula,numPlaza,pinPlaza)

    elif op=='2':
        print("Pulse 1 para depositar su vehiculo\n"
              "Pulse 2 para retirar su vehiculo")
    elif op=='3':
        print('F')
# print("matriculas")
# pickle_in = open("./pickleData/VehiculosDB","rb")
# c = pickle.load(pickle_in)
# for i in c.keys():
#     print(i)
#
# print("Tickets")
# pickle_in1 = open("./pickleData/TicketDB","rb")
# c1= pickle.load(pickle_in1)
# print(c1)

pickle_in=open("./pickleData/PlazasDB")
plazasL=pickle.load(pickle_in)
print(plazasL)
