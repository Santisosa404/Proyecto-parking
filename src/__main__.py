from datetime import datetime

from src.Controller.AdminController import AdminControler
from src.Controller.ParkingController import ParkingController
from src.Models.Abonado import Abonado
from src.Models.Admin import Admin
from src.Models.MovRed import MovRed
from src.Models.Motocicleta import Motocicleta
from src.Models.Parking import Parking
from src.Models.Plaza import Plaza
from src.Models.Ticket import Ticket
from src.Models.Turismo import Turismo
import pickle

from src.Repository.AbonadoRepository import AbonadoRepositorio
from src.Repository.AdminRepository import AdminRepositorio
from src.Repository.PlazaRepository import PlazaRepositorio
from src.Repository.TicketRepository import TicketRepositorio
from src.Repository.VehiculoRepository import VehiculoRepositorio
from src.Service.AbonadoService import AbonadoServicio
from src.Service.AdminService import AdminServicio
from src.Service.ParkingService import Parkingservice
from src.Service.PlazaService import PlazaService
from src.Service.TicketService import TicketServicio
from src.Service.VehiculoService import VehiculoService

plazasParking = int(input("Antes de comenzar, debo saber de cuantas plazas será el parking\n"))

v1 = Turismo('2323')
m1 = Motocicleta('7777', datetime(2020, 1, 1), datetime.now())
pla1 = Plaza(77, v1, 1234, True)
v1.Plaza = pla1
pla1.Vehiculo = v1
dicVehiculos = dict()
dicVehiculos[v1.matricula] = v1
abo = Abonado("Santiago", "Sosa Díaz", "77873839W", v1, pla1, "1234 1234 1234 1234", "Anual",
              "sosa.disan20@triana.salesianos.edu", datetime.now(), datetime(2021, 12, 16))
admin = Admin("Luismi", "MiClave123")
t2 = Ticket(m1, True)
dicPlazas = dict()
dicPlazas['77'] = pla1
dicTicket = dict()
dicTicket[t2.Vehiculo.matricula] = t2
dicAbonados = dict()
dicAbonados[abo.dni] = abo
dicAdmin = dict()
dicAdmin[admin.clave] = admin

pickle_Admin = open("./pickleData/AdminDB", "wb")
pickle.dump(dicAdmin, pickle_Admin)
pickle_Admin.close()

pickle_abonado = open("./pickleData/AbonadosDB", "wb")
pickle.dump(dicAbonados, pickle_abonado)
pickle_abonado.close()

pickle_ticket = open("./pickleData/TicketDB", "wb")
pickle.dump(dicTicket, pickle_ticket)
pickle_ticket.close()

pickle_Vehiculos = open("./pickleData/VehiculosDB", "wb")
pickle.dump(dicVehiculos, pickle_Vehiculos)
pickle_Vehiculos.close()

pickle_Plazas = open("./pickleData/PlazasDB", "wb")
pickle.dump(dicPlazas, pickle_Plazas)
pickle_Plazas.close()

# pickle_in=open("./pickleData/VehiculosDB","rb")
# Vehiculos_in=pickle.load(pickle_in)
# print(Vehiculos_in.keys())

p1 = Parking(dicVehiculos, plazasParking)
parkingServicio = Parkingservice(p1)

vehiculoRepositorio = VehiculoRepositorio()
vehiculoServicio = VehiculoService(vehiculoRepositorio, dicVehiculos)

plazaRepositorio = PlazaRepositorio()
plazaServicio = PlazaService(plazaRepositorio, dicPlazas)

ticketRepositorio = TicketRepositorio()
ticketServicio = TicketServicio(ticketRepositorio, dicTicket)

abonadoRepositorio = AbonadoRepositorio()
abonadoServicio = AbonadoServicio(abonadoRepositorio, dicAbonados)

adminRepositorio = AdminRepositorio()
adminServicio = AdminServicio(adminRepositorio, dicAdmin)

parkingController = ParkingController(parkingServicio, vehiculoServicio, plazaServicio, ticketServicio)
adminController = AdminControler(ticketServicio,abonadoServicio)
op = -1

while op != '0':
    print('Bienvendio al parking Bustillo 2.0.\n'
          'Pulse 1 para hacer uso del parking sin abono\n'
          'Pulse 2 para hacer uso del parking con abono\n'
          'Pulse 3 para acceder a la administracion del parking')
    op = input()
    if op == '1':
        op1 = -1
        while op1 != '0':
            print(parkingController.estadoParking())
            print("Pulse 1 para depositar el vehiculo\n"
                  "Pulse 2 para retirar el vehiculo")
            op1 = input()
            if op1 == '1':
                tipo = input('¿Qué vehiculo va a depositar?\n')
                matricula = input('Matricula del vehiculo a ingresar\n')
                if tipo.lower() == 'turismo':
                    vehiculo = Turismo(matricula)
                elif tipo.lower() == 'motocicleta':
                    vehiculo = Motocicleta(matricula)
                elif tipo.lower() == 'movilidad reducida':
                    vehiculo = MovRed(matricula)
                parkingController.depositarVehiculo(vehiculo)
            elif op1 == '2':
                matricula = input("Para retirar el vehiculo será requerido:\n"
                                  "Matricula del vehiculo:")
                numPlaza = input('Plaza asignada: ')
                pinPlaza = int(input('Pin asociado: '))
                parkingController.retirarVehiculo(matricula, numPlaza, pinPlaza)

    elif op == '2':
        print("Introduzca sus datos para acceder a su parking personal.")
        dni = input("Dni:")
        matricula = input("Matricula:")
        if abonadoServicio.comprobarAbonado(dni, matricula):
            abonadoActual = abonadoServicio.buscarPorDni(dni)
            op2 = -1
            while op2 != '0':
                op2 = input("Pulse 1 para depositar su vehiculo\n"
                            "Pulse 2 para retirar su vehiculo")
                print(op2)
                if op2 == '1':
                    parkingController.depositarVehiculoAbonado(abonadoActual)
                elif op2 == '2':
                    parkingController.retirarVehiculoAbonado(abonadoActual)

        else:
            print("Crendenciales incorrectas")
    elif op == '3':
        nombre = input('Para entrar la zona de la administracion debera loguearse.\n'
                       'Introduzca su nombre: ')
        clave = input('Introduzca su clave de acceso: ')
        if adminServicio.comprobarClave(nombre, clave):
            adminServicio.buscarPorClave(clave)
            print(f"\nBienvenido {admin.nombre}")
            op3 = -1
            while op3 != 0:
                op3 = input("Pulse 1 para ver el estado del parking\n"
                            "Pulse 2 para la facturacion entre fechas\n"
                            "Pulse 3 para consultar los Abonados\n"
                            "Pulse 4 para gestionar los Abonos\n"
                            "Pulse 5 para ver la caducidad de los Abonos\n")
                if op3 == '1':
                    print(parkingController.estadoParking())
                elif op3 == '2':
                    print("Para ver la facturacion introduzca dos fechas para buscar en formato DD-MM-YYYY MM:SS")
                    date_entry1 = input('Primera fecha: ')
                    fecha1 = adminController.convertirFecha(date_entry1)
                    date_entry2 = input('Primera fecha: ')
                    fecha2 = adminController.convertirFecha(date_entry2)
                    adminController.imprimirFacturacion(fecha1, fecha2)

                elif op3 == '3':
                    adminController.imprimirAbonados()
                elif op3 == '4':
                    print("TODO")
                elif op3 == '5':
                    print("TODO")
        else:
            print("Credenciales incorrectas")


