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
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []
    
    def registra_comprar(self, compra):
        self.compras.append(Compra(compra))
    
    def get_data_ultima_compra(self):
        return self.compras[-1] if self.compras[-1] else 'não tem compras feitas'
    
    def total_compras(self):
        valor += valor
        return valor


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


class Compra:
    def __init__(self, vendedor, valor):
        self.vendedor = vendedor
        self.data = datetime.now()
        self.valor = valor

        
