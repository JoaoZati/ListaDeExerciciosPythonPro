"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""

class CirculoPerfeito:
    def __init__(self):  #dander init double _
        self.cor = 'Neutro'
        self.circunferencia = 1
        self.material = 'Papel'
    
    def mostra_id(self): #pode ser qualquer nome, convensão self
        return id(self)
    
    def mostra_cor(self):
        return self.cor
    
    def troca_cor(self, cor):
        self.cor = cor

circulo_primeiro = CirculoPerfeito()
circulo_segundo = CirculoPerfeito()

print(type(circulo_primeiro))
print(circulo_primeiro == circulo_segundo)
print(id(circulo_primeiro), circulo_primeiro.mostra_id()) 
print(id(circulo_segundo), circulo_segundo.mostra_id())

circulo_segundo.cor = 'Amarelo' 
print(circulo_primeiro.cor, circulo_segundo.cor)
print(circulo_primeiro.mostra_cor())

circulo_segundo.troca_cor('Vermelho')
print(circulo_segundo.cor)
