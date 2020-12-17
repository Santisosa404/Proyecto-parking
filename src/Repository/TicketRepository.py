import pickle
class TicketRepositorio():
    def __init__(self, ticketDB=open("./pickleData/TicketDB","rb")):
        self._ticketDB=ticketDB

    @property
    def ticketDB(self):
        return self._ticketDB

    def agregarTicket(self,dicTicket):
        self.ticketDB.close()
        pickle_in = open("./pickleData/TicketDB","wb")
        pickle.dump(dicTicket,pickle_in)
        pickle_in.close()
        self._ticketDB = open("./pickleData/TicketDB","rb")

    def buscarTicketPagados(self):
        datos = pickle.load(self.ticketDB)
        dicPagados=dict()
        for i in datos.values():
            if i.pagado:
                dicPagados[i.Vehiculo.matricula]=i
        return dicPagados


