#%% 12 - Classe contade investimento

"""
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja 
semelhante a classe contaBancaria, com a diferença de que se adicione um 
atributo taxaJuros. Forneça um construtor que configure tanto o saldo 
inicial como a taxa de juros. Forneça um método adicioneJuros (sem 
parâmetro explícito) que adicione juros à conta. Escreva um programa 
que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa 
de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e 
imprime o saldo resultante.
"""

class ContaInvestimento:
    def __init__(self, saldo_inicial: float, taxa_juros: float):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros/100
        
    def deposito(self, quantia):
        if quantia <= 0:
            print('Insira uma quantia positiva para deposito')
        else: self.saldo += quantia
    
    def saque(self, quantia):
        if quantia <= 0:
            print('Insira uma quantia positiva para saque')
        else: self.saldo -= quantia
        
    def valorizacao(self, tempo: int):
        try: tempo = int(tempo)
        except ValueError: return
        
        print(f'Saldo antigo {self.saldo:.2f}')
        self.saldo *= (1 + self.taxa_juros)**tempo
        print(f'Saldo Novo {self.saldo:.2f}')
        
    def adicione_juros(self):
        print(f'Saldo antigo {self.saldo:.2f}')
        self.saldo *= (1 + self.taxa_juros)
        print(f'Saldo Novo {self.saldo:.2f}')
        
    def imprimir_saldo(self):
        print(f'O saldo é de {self.saldo:.2f}')
        
conta = ContaInvestimento(1000, 10)
for _ in range(5): conta.adicione_juros()
conta.saque(500)
conta.imprimir_saldo()
conta.valorizacao(2)
