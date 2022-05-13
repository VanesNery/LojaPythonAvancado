#! usr/local/bin/python3

from .compra import Compra
from .pessoa import Pessoa


def get_compra(compra):
    return compra.data


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []
    
    def registrar_compra(self, compra):
        self.compras.append(compra)
    
    def get_data_ultima_compra(self):
        return None if not self.compras else \
            sorted(self.compras, key=get_compra)[-1].data
    
    def total_compras(self):
        for compra in self.compras:
            compra.valor += compra.valor
        return compra.valor
