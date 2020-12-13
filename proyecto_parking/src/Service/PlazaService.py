class PlazaService():
    def __init__(self,Plaza):
        self._Plaza=Plaza

    @property
    def Plaza(self):
        return self._Plaza
    @Plaza.setter
    def Plaza(self,Plaza):
        self._Plaza=Plaza

