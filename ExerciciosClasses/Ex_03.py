#%% 03 - Classe Retangulo

"""

Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a 
escolher)

Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área 
e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que 
informe as medidades de um local. Depois, deve criar um objeto com as 
medidas e calcular a quantidade de pisos e de rodapés necessárias para 
o local.

"""

class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self.base = base
        self.altura = altura
        
    def mudar_valor_lados(self, base = False, altura = False):
        if base: self.base = base
        if altura: self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2*(self.base + self.altura)
    
def inserir_float(menssagem: str):
    while True:
        try:
            num = float(input(menssagem))
            if num > 0: return num
            print('Insira um valor maior igual a 0')
        except ValueError: print('Insira um número')
            

base_local = inserir_float('Base Local: ')
altura_local = inserir_float('Altura Local: ')
base_piso = inserir_float('Base Piso: ')
altura_piso = inserir_float('Altura Piso: ')
comprimento_rodape = inserir_float('Comprimento Rodape: ')

piso = Retangulo(base = base_piso, altura = altura_piso)
rodape = Retangulo(base = comprimento_rodape)
area_local = Retangulo(base = base_local, altura = altura_local)

quantidade_pisos = area_local.calcular_area() / piso.calcular_area()
quantidade_rodapes = area_local.calcular_perimetro() / rodape.base

print(f'A quantidade de pisos a usar é {quantidade_pisos} e a '
      f'Quantidade de rodapes a ser usado é {quantidade_rodapes} ')
