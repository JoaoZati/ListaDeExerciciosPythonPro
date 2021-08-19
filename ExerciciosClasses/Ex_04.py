#%% 04 - Classe Pessoa

"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a 
cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 
anos, ela deve crescer 0,5 cm.
"""

class Pessoa:
    def __init__(self, nome: str, idade: str, peso: str, altura: str):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self, anos = 1):
        if anos < 0:
            print('Uma pessoa não volta no tempo')
            return
        if self.idade < 21: self.altura += anos * 0.05
        self.idade += anos
        
    def engordar(self, peso = 1):
        if peso < 0:
            print('Peso negativo significa que a pessoa emagreceu')
            return
        self.peso += peso
        
    def emagrecer(self, peso = 1):
        if peso < 0:
            print('Usar um valor positivo (a pessoa perder x peso)')
            return
        self.peso -= peso
        
    def crescer(self, altura = 0.1):
        self.altura += altura
        
joao = Pessoa('Joao', 27, 85, 1.81)
leo = Pessoa('Leonardo', 18, 72, 1.70)

print(joao.idade)
joao.envelhecer(-2)
print(joao.idade)
print(joao.altura)
joao.envelhecer(1)
print(joao.altura, joao.idade, joao.peso)
joao.emagrecer(-1)
joao.emagrecer(2)
print(joao.peso)
print('Leo', leo.idade, leo.altura )
leo.envelhecer(2)
print('Leo', leo.idade, leo.altura )
