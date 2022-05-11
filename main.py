#! usr/local/bin/python3
from datetime import datetime


class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'Nome: {self.nome} e sua idade é: {self.idade}'
    
    def is_adulto(self):
        if self.idade >= 20:
            return f'É Adulto'
        else:
            return f'É criança'


class Cliente(Pessoa):
    compras = []
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def registrar_comprar(self, compra):
        pass
    
    def get_data_ultima_compra(self):
        pass
    
    def total_compras(self):
        pass


class Vendedor(Pessoa):
    
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

