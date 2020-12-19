import random
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
# Vehiculos

v1 = Turismo('2323-CRY', datetime(2020, 12, 12))
v2 = Turismo('1212-RKO', datetime(2020, 12, 13))
v3 = Turismo('5344-AFK', datetime(2020, 12, 14), datetime.now())
v4 = Turismo('3244-KFC', datetime(2020, 12, 15), datetime.now())

m1 = Motocicleta('7777-GPU', datetime(2020, 12, 12))
m2 = Motocicleta('8976-GTX', datetime(2020, 12, 13))
m3 = Motocicleta('4676-RTX', datetime(2020, 12, 15), datetime.now())
m4 = Motocicleta('2346-CPU', datetime(2020, 12, 14), datetime.now())

mR1 = MovRed('3456-XDD', datetime(2020, 12, 12))
mR2 = MovRed('7899-XDD', datetime(2020, 12, 13))
mR3 = MovRed('9898-XDD', datetime(2020, 12, 14), datetime.now())
mR4 = MovRed('9898-XDD', datetime(2020, 12, 15), datetime.now())

# Plazas
pla1 = Plaza(77, v1, 123456, True)
pla2 = Plaza(78, v2, 654321, True)
pla3 = Plaza(79, m1, 123456, True)
pla4 = Plaza(80, m2, 654321, True)
pla5 = Plaza(81, mR1, 123456, True)
pla6 = Plaza(82, mR2, 654321, True)

v1.Plaza = pla1
v2.Plaza = pla2
m1.Plaza = pla3
m2.Plaza = pla4
mR1.Plaza = pla5
mR2.Plaza = pla6

# Tickets
t1 = Ticket(v3, True)
t2 = Ticket(v4, True)
t3 = Ticket(m3, True)
t4 = Ticket(m4, True)
t5 = Ticket(mR3, True)
t6 = Ticket(mR4, True)

# Abonados

ab1 = Abonado("Santiago", "Abonado 1", "77873839A", v1, pla1, "1234 1234 1234 1234", "Anual",
              "abonado1@correo.com", datetime.now(), datetime.now().replace(year=datetime.now().year + 1))
ab2 = Abonado("Santiago", "Abonado 2", "77873839B", v2, pla2, "1234 1234 1234 1234", "Mensual",
              "abonado2@correo.com", datetime.now(), datetime.now().replace(month=+1))
ab3 = Abonado("Santiago", "Abonado 3", "77873839C", m1, pla3, "1234 1234 1234 1234", "Mensual",
              "abonado3@correo.com", datetime.now(), datetime.now().replace(month=+1))
ab4 = Abonado("Santiago", "Abonado 4", "77873839D", m2, pla4, "1234 1234 1234 1234", "Anual",
              "abonado4@correo.com", datetime.now(), datetime.now().replace(year=datetime.now().year + 1))
ab5 = Abonado("Santiago", "Abonado 5", "77873839E", mR1, pla5, "1234 1234 1234 1234", "Semestral",
              "abonado5@correo.com", datetime.now(), datetime.now().replace(month=+6))
ab6 = Abonado("Santiago", "Abonado 6", "77873839F", mR2, pla6, "1234 1234 1234 1234", "Trimestral",
              "abonado6@correo.com", datetime.now(), datetime.now().replace(month=+3))

admin = Admin("Luismi", "MiClave123")

dicVehiculos=dict()
dicVehiculos = {v1.matricula: v1, v2.matricula: v2, v3.matricula: v3, v4.matricula: v4, m1.matricula: m1,
                m2.matricula: m2, m3.matricula: m3, m4.matricula: m4, mR1.matricula: mR1, mR2.matricula: mR2,
                mR3.matricula: mR3, mR4.matricula: mR4}

dicPlazas=dict()
dicPlazas = {str(pla1.numPlaza): pla1, str(pla2.numPlaza): pla2, str(pla3.numPlaza): pla3, str(pla4.numPlaza): pla4,
             str(pla5.numPlaza): pla5, str(pla6.numPlaza): pla6}

dicTicket=dict()
dicTicket = {t1.Vehiculo.matricula: t1, t2.Vehiculo.matricula: t2, t3.Vehiculo.matricula: t3, t4.Vehiculo.matricula: t4,
             t5.Vehiculo.matricula: t5, t6.Vehiculo.matricula: t6}

dicAbonados=dict()
dicAbonados = {ab1.dni: ab1, ab2.dni: ab2, ab3.dni: ab3, ab4.dni: ab4, ab5.dni: ab5, ab6.dni: ab6}

dicAdmin = dict()
dicAdmin[admin.clave] = admin

# Carga a bases de datos
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
adminController = AdminControler(ticketServicio, abonadoServicio)

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
                    pin = input('Para retirar el vehiculo será requerido el pin\n'
                                'Pin: ')
                    parkingController.depositarVehiculoAbonado(abonadoActual, pin)
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
            while op3 != '0':
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
                    op4 = -1
                    while op4 != '0':
                        op4 = input("Pulse 1 para dar de Alta a un Abonado\n"
                                    "Pulse 2 para modificar un Abonado\n"
                                    "Pulse 3 para dar de baja a un Abonado")
                        if op4 == '1':
                            print('Para dar de alta necesitaré sus datos personales')
                            nombre = input('Nombre del Abonado: ')
                            apellidos = input('Apellidos del Abonado: ')
                            dni = input('Dni: ')
                            email = input('Email: ')
                            numTarjeta = input('Numero de tarjeta: ')
                            tipoVehiculo = input('Tipo de vehiculo a estacionar: ')
                            matricula = input('Matricula del turismo: ')
                            pin = int(input('Pin del abonado: '))
                            tipoAbono = input('Tipo Abono: ')

                            if tipoVehiculo.lower() == 'turismo':
                                VehiculoAbonado = Turismo(matricula)
                            elif tipoVehiculo.lower() == 'motocicleta':
                                VehiculoAbonado = Motocicleta(matricula)
                            elif tipoVehiculo.lower() == 'movilidad reducida':
                                VehiculoAbonado = MovRed(matricula)

                            PlazaAbonado = Plaza(random.randint(1, p1.plazasTotales), VehiculoAbonado, pin, True)
                            VehiculoAbonado.Plaza = PlazaAbonado
                            if adminController.darDeAlta(nombre, apellidos, dni, email, numTarjeta, VehiculoAbonado,
                                                         PlazaAbonado, tipoAbono):
                                print('Abonado dado de alta')
                            else:
                                print('No ha sido posible agregar el abonado')

                        elif op4 == '2':
                            dniOld = input('Indique el dni del Abonado a modificar')
                            abonado = abonadoServicio.buscarPorDni(dniOld)
                            op5 = input('Pulse 1 para cambiar los datos personales\n'
                                        'Pulse 2 para renovar la fecha de cancelación')
                            if op5 == '1':
                                nombre = input('Nombre del Abonado: ')
                                apellidos = input('Apellidos del Abonado: ')
                                correo = input('Correo del Abonado: ')
                                dni = input('Dni del Abonado: ')
                                adminController.modificarAbonado(abonado, nombre, apellidos, correo, dni, dniOld)
                            elif op5 == '2':
                                print('El pago se cobrara en la tarjeta del abonado')
                                adminController.renovarCancelacion(abonado)
                                print('La fecha de cancelacion a sido correctamente renovada')
                        elif op4 == '3':
                            dniBorrar = input('Indique el dni del abonado a eliminar: ')
                            abonadoBorrar = abonadoServicio.buscarPorDni(dniBorrar)
                            op6 = input(f'El abonado {abonadoBorrar.nombre} {abonadoBorrar.apellidos} sera eliminado.\n'
                                        f'Pulse 1 para confirmar la baja.\n'
                                        f'Pulse cualquier otra tecla para cancelar')
                            if op6 == '1':
                                adminController.darDeBaja(abonadoBorrar)
                            else:
                                print('Operación cancelada')
                        else:
                            print("Opción incorrecta")
                elif op3 == '5':
                    op7 = input('Pulse 1 para consultar de los abonos sobre un mes.\n'
                                'Pusle 2 para consultar los abonos que caduquen en un plazo de 10 dias\n ')
                    if op7 == '1':
                        mes = input('Indique el mes en formato numerico sobre el que buscar: ')
                        adminController.imprimirConsulta(mes)
                    elif op7 == '2':
                        adminController.imprimirConsulta()

        else:
            print("Credenciales incorrectas")
