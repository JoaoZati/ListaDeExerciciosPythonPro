#%% 10 - Classe Bomba de Combustivel

"""
Classe Bomba de Combustível: Faça um programa completo utilizando 
classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses 
atributos:
    
tipoCombustivel.
valorLitro
quantidadeCombustivel

Possua no mínimo esses métodos:
    
abastecerPorValor( ) – método onde é informado o valor a ser abastecido 
e mostra a quantidade de litros que foi colocada no veículo

abastecerPorLitro( ) – método onde é informado a quantidade em litros de 
combustível e mostra o valor a ser pago pelo cliente.

alterarValor( ) – altera o valor do litro do combustível.

alterarCombustivel( ) – altera o tipo do combustível.

alterarQuantidadeCombustivel( ) – altera a quantidade de combustível 
restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a 
quantidade de combustível total na bomba.
"""

#Bastante pratica sobre encapsulamento (valor negativo de litros)

class BombaCombustível:
    def __init__(self, tipo_combustivel: str, valor_litro: float, quantidade_combustivel: float):
        self.valor_litro = valor_litro
        self.tipo_combustivel = tipo_combustivel
        self.quantidade_combustivel = quantidade_combustivel
        
    def abastecer_por_valor(self, valor: float):
        litros_abastecidos = valor / self.valor_litro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)   
    
    def _apresentar_abastecimento_se_possivel(self, litros_abastecidos: float, valor:float):
        if litros_abastecidos > self.quantidade_combustivel:
            litros_faltantes = litros_abastecidos - self.quantidade_combustivel
            print(f'Não é possivel abastecer, faltam {litros_faltantes:.2f} litros na bomba')
            print('Reabasteça a Bomba')
            return
        
        self.quantidade_combustivel -= litros_abastecidos
        print(f'Foram abastecidos {litros_abastecidos:.2f} litros no valor de R$ {valor:.2f}')
        print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel}')
        print('')
        
    def abastecer_por_litros(self, litros_abastecidos: float):
        valor = litros_abastecidos * self.valor_litro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)
        
    def adicionar_combustivel_bomba(self, quantidade: float):
        if quantidade >= 0: self.quantidade_combustivel += quantidade
        else: print('Malandrinho, você não vai roubar gasolina')
            
        
    
bomba = BombaCombustível('Gasolina', 4.59, 100.0)
bomba.abastecer_por_valor(25.0)
bomba.abastecer_por_litros(80)

bomba.valor_litro = 5.59
bomba.abastecer_por_litros(50)

bomba.adicionar_combustivel_bomba(-20)
bomba.adicionar_combustivel_bomba(50)
print(f'{bomba.quantidade_combustivel:.2f}')
