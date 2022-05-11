#! usr/local/bin/python3
from poo.desafio_poo.pessoa import Pessoa


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
