#%% 07 - Classe Bichinho Virtual

"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi 
(Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, 
Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma 
informação que devemos levar em consideração, o Humor do nosso 
tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, 
ou seja, um campo calculado, então não devemos criar um atributo para 
armazenar esta informação por que ela pode ser calculada a qualquer 
momento.
"""

class Tamagushi:
    def __init__(self, nome: str, fome = 0, saude = 100, idade = 1):
        try: int(fome), int(saude), int(idade)
        except ValueError: 
            self.nome, self.fome, self.saude, self.idade = nome, 0, 100, 1
            self.humor = self.saude - self.fome - self.idade
            return
        
        self.nome, self.fome, self.saude, self.idade = nome, fome, saude, idade
        self.humor = self.saude - self.fome - self.idade
        
        
    def alterar_nome(self, nome: str):
        self.nome = nome
        
    def alterar_fome(self, fome: int):
        try: int(fome)
        except ValueError: return
        
        self.fome += fome
        self.humor = self.saude - self.fome - self.idade
    
    def alterar_idade(self, idade: int):
        try: int(idade)
        except ValueError: return
        
        if idade < 0: return
        
        self.idade += idade
        self.humor = self.saude - self.fome - self.idade
        
    def alterar_saude(self, saude: int):
        try: int(saude)
        except ValueError: return
        
        self.saude += saude
        self.humor = self.saude - self.fome - self.idade
        
minigun = Tamagushi('Minigun')
mau = Tamagushi('Mau', saude = 'abobora')

minigun.alterar_idade(1)
minigun.alterar_idade(-1)
mau.alterar_fome(5)

minigun.alterar_saude(5)
