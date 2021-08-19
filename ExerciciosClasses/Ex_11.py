#%% 11 - Classe Carro

"""
Classe carro: Implemente uma classe chamada Carro com as seguintes 
propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e 
uma certa quantidade de combustível no tanque.

O consumo é especificado no construtor e o nível de combustível inicial 
é 0.

Forneça um método andar( ) que simule o ato de dirigir o veículo por uma 
certa distância, reduzindo o nível de combustível no tanque de gasolina.

Forneça um método obterGasolina( ), que retorna o nível atual de 
combustível.

Forneça um método adicionarGasolina( ), para abastecer o tanque. 
Exemplo de uso:
    
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
"""

class Carro:
    def __init__(self, consumo_de_combustivel:float):
        
        self.combustivel_tanque = 0
        
        if consumo_de_combustivel <= 0: 
            print('Consumo de combustivel tem que ser maior que zero, por padrão sera setado em 10.0')
            self.consumo_de_combustivel = 10.0
            return
        
        self.consumo_de_combustivel = consumo_de_combustivel
    
    def _verificacao(self):
        try:
            float(self.combustivel_tanque)
            float(self.consumo_de_combustivel)
        except ValueError: return False
        
        if self.combustivel_tanque < 0 or self.consumo_de_combustivel <= 0: return False
        return True
    
    def andar(self, distancia: float):
        if not self._verificacao():
            print('Existe um problema: verifique se consumo de combustivel tem valor maior que 0 e combustivel tanque tem valor positivo e são floats')
            return
        
        if self.combustivel_tanque == 0: 
            print('Carro nao pode andar, sem gasolina')
            return
        
        combustivel_usado = distancia / self.consumo_de_combustivel
        if combustivel_usado > self.combustivel_tanque:
            distancia_percorrida = self.combustivel_tanque * self.consumo_de_combustivel
            self.combustivel_tanque = 0
            print(f'O carro andou {distancia_percorrida} e possui {self.combustivel_tanque} de gasolina sobrando')
            return
        
        self.combustivel_tanque -= combustivel_usado
        print(f'Carro andou {distancia:.2f} quilometros, gastou {combustivel_usado:.2f} litros')
        
    def adicionar_gasolina(self, gasolina: float):
        if not self._verificacao():
            print('Existe um problema: verifique se consumo de combustivel tem valor maior que 0 e combustivel tanque tem valor positivo e são floats')
            return
        
        if gasolina < 0: 
            print('Você não pode retirar gasolina nesse metodo')
            return
        
        self.combustivel_tanque += gasolina
        
    def obter_gasolina(self):
        if not self._verificacao():
            print('Existe um problema: verifique se consumo de combustivel tem valor maior que 0 e combustivel tanque tem valor positivo e são floats')
            return
        
        print(self.combustivel_tanque)
        
meuFusca = Carro(15)
meuFusca.adicionar_gasolina(20)
meuFusca.andar(100)
meuFusca.obter_gasolina()
meuFusca.adicionar_gasolina(10)
meuFusca.obter_gasolina()
meuFusca.adicionar_gasolina(-5)
meuFusca.consumo_de_combustivel = -1
meuFusca.andar(5)
meuFusca.obter_gasolina()
