#! usr/local/bin/python3

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'Nome: {self.nome} e sua idade é: {self.idade}'
    
    def is_adulto(self):
        if self.idade >= 18:
            return f'É Adulto'
        else:
            return f'É criança'