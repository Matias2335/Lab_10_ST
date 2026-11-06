CUPONS = {"DEZ": 10, "VINTE": 20}  # codigo -> porcentagem de desconto
MINIMOS = {"DEZ": 10000, "VINTE": 30000}  # codigo -> subtotal minimo


class Carrinho:
    def __init__(self):
        self._subtotal = 0
        self._desconto = 0
        self._minimo = 0

    def adicionar(self, preco, quantidade=1):
        if preco <= 0:
            raise ValueError("preco deve ser positivo")
        if not isinstance(quantidade, int) or quantidade < 1:
            raise ValueError("quantidade deve ser inteira e ao menos 1")
        self._subtotal += preco * quantidade

    def aplicar_cupom(self, codigo):
        if codigo not in CUPONS:
            raise ValueError("cupom desconhecido")
        self._desconto = CUPONS[codigo]
        self._minimo = MINIMOS[codigo]

    @property
    def total(self):
        if self._subtotal < self._minimo:
            return self._subtotal
        return self._subtotal * (100 - self._desconto) // 100
