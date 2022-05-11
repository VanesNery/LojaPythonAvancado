#! usr/local/bin/python3

from poo.desafio_poo.pessoa import Compra
from poo.desafio_poo.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []
    
    def registra_comprar(self, compra):
        self.compras.append(Compra(compra))
    
    def get_data_ultima_compra(self):
        return self.compras[-1] if self.compras[-1] else 'não tem compras feitas'
    
    def total_compras(self):
        for compra in self.compras:
            total_compra = compra.valor + compra.valor
        return total_compra
