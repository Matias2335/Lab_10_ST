class Fila:
    @property
    def aguardando(self):
        return 0
class Fila:
    def emitir(self, tipo):
        return "N1"

    @property
    def aguardando(self):
        return 0
class Fila:
    def __init__(self):
        self._emitidas = 0

    def emitir(self, tipo):
        self._emitidas += 1
        return f"N{self._emitidas}"

    @property
    def aguardando(self):
        return 0