from src.Models.Ticket import Ticket


class TicketServicio():
    def __init__(self, ticketRepositorio, dicTicket):
        self._ticketRepositorio = ticketRepositorio
        self._dicTicket = dicTicket

    @property
    def ticketRepositorio(self):
        return self._ticketRepositorio

    @property
    def dicTicket(self):
        return self._dicTicket

    def generarTicket(self, Vehiculo):
        ticket = Ticket(Vehiculo, False)
        self.dicTicket[Vehiculo.matricula] = ticket
        self.ticketRepositorio.agregarTicket(self.dicTicket)
        print("********** Impriminedo Ticket **********\n")
        print(ticket)

    def generarTicketSalida(self, Vehiculo):
        ticket = Ticket(Vehiculo, True)
        self.dicTicket[Vehiculo.matricula] = ticket
        self.ticketRepositorio.agregarTicket(self.dicTicket)
        print("********** Impriminedo Ticket **********\n")
        print(ticket)

    def facturacionFechas(self, fecha1, fecha2):
        dicPagados = self.ticketRepositorio.buscarTicketPagados()
        result = dict()
        for i, j in dicPagados.items():
            if fecha1 <= j.Vehiculo.fechaSalida <= fecha2:
                result[i] = j
        return result
