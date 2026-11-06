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
class Fila:
    def __init__(self):
        self._emitidas = {"normal": 0, "prioritaria": 0}

    def emitir(self, tipo):
        self._emitidas[tipo] += 1
        prefixo = "N" if tipo == "normal" else "P"
        return f"{prefixo}{self._emitidas[tipo]}"

    @property
    def aguardando(self):
        return 0
class Fila:
    def __init__(self):
        self._emitidas = {"normal": 0, "prioritaria": 0}

    def emitir(self, tipo):
        if tipo not in self._emitidas:
            raise ValueError("tipo invalido")
        self._emitidas[tipo] += 1
        prefixo = "N" if tipo == "normal" else "P"
        return f"{prefixo}{self._emitidas[tipo]}"

    @property
    def aguardando(self):
        return 0

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
        raise IndexError("fila vazia")
    def chamar(self):
        if not self._espera["normal"]:
            raise IndexError("fila vazia")
        return self._espera["normal"].pop(0)
    def chamar(self):
        if self._espera["prioritaria"] and not (
            self._seguidas >= 2 and self._espera["normal"]
        ):
            self._seguidas += 1
            return self._espera["prioritaria"].pop(0)
        if self._espera["normal"]:
            return self._espera["normal"].pop(0)
        raise IndexError("fila vazia")
    
    