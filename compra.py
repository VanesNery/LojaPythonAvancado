#! usr/local/bin/python3
from datetime import datetime

class Compra:
    def __init__(self, vendedor, valor):
        self.vendedor = vendedor
        self.data = datetime.now()
        self.valor = valor

