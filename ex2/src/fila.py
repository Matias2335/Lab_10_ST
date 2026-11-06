class Fila:
    def __init__(self):
        self._emitidas = {"normal": 0, "prioritaria": 0}
        self._espera = {"normal": [], "prioritaria": []}
        self._seguidas = 0

    def emitir(self, tipo):
        if tipo not in self._emitidas:
            raise ValueError("tipo invalido")
        self._emitidas[tipo] += 1
        prefixo = "N" if tipo == "normal" else "P"
        senha = f"{prefixo}{self._emitidas[tipo]}"
        self._espera[tipo].append(senha)
        return senha

    @property
    def aguardando(self):
        return len(self._espera["normal"]) + len(self._espera["prioritaria"])

    def chamar(self):
        if self._espera["prioritaria"] and not (
            self._seguidas >= 2 and self._espera["normal"]
        ):
            self._seguidas += 1
            return self._espera["prioritaria"].pop(0)
        if self._espera["normal"]:
            self._seguidas = 0
            return self._espera["normal"].pop(0)
        raise IndexError("fila vazia")
