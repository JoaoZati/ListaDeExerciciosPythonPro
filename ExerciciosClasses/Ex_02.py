"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado():
    def __init__(self, tamanho_lado: float):
        self.tamanho_lado = tamanho_lado
        
    def criar_valor_lado(self, lado: float):
        self.valor_lado = lado
        
    def mudar_tamanho_lado(self, lado:float):
        self.tamanho_lado = lado
    
    def retornar_tamanho_lado(self):
        return self.tamanho_lado
    
    def calcular_area(self):
        return self.tamanho_lado**2
    
quadrado1 = Quadrado(2.5)
quadrado2 = Quadrado(3.2)

print(quadrado1.tamanho_lado, quadrado2.tamanho_lado)
print(quadrado1.retornar_tamanho_lado(), quadrado2.retornar_tamanho_lado())

quadrado1.criar_valor_lado(5)
print(quadrado1.retornar_tamanho_lado())

quadrado2.mudar_tamanho_lado(4.5)
print(quadrado2.retornar_tamanho_lado())

print(quadrado1.calcular_area(), quadrado2.calcular_area())
