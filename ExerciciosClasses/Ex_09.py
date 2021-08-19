#%% 09 - Classe Ponto e Retangulo

"""
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e 
classes que:

Possua uma classe chamada Ponto, com os atributos x e y.

Possua uma classe chamada Retangulo, com os atributos largura e altura.

Possua uma função para imprimir os valores da classe Ponto

Possua uma função para encontrar o centro de um Retângulo.

Você deve criar alguns objetos da classe Retangulo.

Cada objeto deve ter um vértice de partida, por exemplo, o vértice 
inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.

A função para encontrar o centro do retângulo deve retornar o valor para 
um objeto do tipo ponto que indique os valores de x e y para o centro do 
objeto.

O valor do centro do objeto deve ser mostrado na tela

Crie um menu para alterar os valores do retângulo e imprimir o centro 
deste retângulo.
"""
from copy import copy

class Ponto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def adicionar_x(self, x):
        self.x += x
        
    def adicionar_y(self, y):
        self.y += y
        
    def imprimir_coordenadas(self):
        print(f'O centro é {self.x}, {self.y}')
        
class Retangulo:
    def alterar_pontos(self):
        self.ponto_centro = copy(self.ponto_inferior_esquerdo)
        self.ponto_centro.adicionar_x(self.largura / 2)
        self.ponto_centro.adicionar_y(self.altura / 2)
        
        self.ponto_inferior_direito = copy(self.ponto_inferior_esquerdo)
        self.ponto_inferior_direito.adicionar_x(self.largura)
        self.ponto_superior_esquerdo = copy(self.ponto_inferior_esquerdo)
        self.ponto_superior_esquerdo.adicionar_y(self.altura)
        
        self.ponto_superior_direito = copy(self.ponto_inferior_esquerdo)
        self.ponto_superior_direito.adicionar_x(self.largura)
        self.ponto_superior_direito.adicionar_y(self.altura)
    
    def __init__(self, largura = 1, altura = 1, ponto_partida = Ponto(0,0)):
        self.largura = largura
        self.altura = altura
        
        self.ponto_inferior_esquerdo = ponto_partida
        self.alterar_pontos()
        
    def imprimir_centro(self):
        self.ponto_centro.imprimir_coordenadas()
        
    def modificar_largura(self, largura):
        self.largura += largura
        self.alterar_pontos()
        
    def modificar_altura(self, altura):
        self.altura += altura
        self.alterar_pontos()
        
    def modificar_ponto_partida(self, ponto_partida):
        self.ponto_inferior_esquerdo = ponto_partida
        self.alterar_pontos()
        
retangulo = Retangulo()
retangulo.imprimir_centro()
print('')

print('Adicionando 1 em largura') 
retangulo.modificar_largura(1)
retangulo.imprimir_centro()

print('Adicionando 1 em altura') 
retangulo.modificar_altura(1)
retangulo.imprimir_centro()

print('Modificando Ponto inicial para 2x2')
retangulo.modificar_ponto_partida(Ponto(2, 2))
retangulo.imprimir_centro()
