#! usr/local/bin/python3
MAIOR_IDADE = 18

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'{self.nome} e sua idade é: {self.idade}'
    
    def is_adulto(self):
        if self.idade >= MAIOR_IDADE:
            return f'É Adulto'
        else:
            return f'É criança'