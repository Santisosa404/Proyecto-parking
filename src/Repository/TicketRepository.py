import pickle
class TicketRepositorio():
    def __init__(self, ticketDB=open("./pickleData/TicketDB","rb")):
        self._ticketDB=ticketDB

    @property
    def ticketDB(self):
        return self._ticketDB

    def agregarTicket(self,dicTicket):
        pickle_in = open("./pickleData/TicketDB","wb")
        pickle.dump(dicTicket,pickle_in)
        pickle_in.close()
