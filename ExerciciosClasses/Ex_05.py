#%% 05 - Classe Conta corrente

"""
Classe Conta Corrente: Crie uma classe para implementar uma conta 
corrente. A classe deve possuir os seguintes atributos: número da conta, 
nome do correntista e saldo. Os métodos são os seguintes: alterarNome, 
depósito e saque; No construtor, saldo é opcional, com valor default 
zero e os demais atributos são obrigatórios.
"""

class ContaCorrente:
    def __init__(self, numero: str, nome: str, saldo = 0):
        if type(numero) != str or len(numero) != 4:
            print('inserir uma string em numero de conta de 4 digitos')
            return
        try: int(numero)
        except ValueError: 
            print('Deve usar apenas numeros para criar conta')
            return
        self.numero_da_conta = numero
        self.nome_correntista = nome
        self.saldo  = saldo
        
    def alterar_nome(self, nome):
        self.nome_correntista = nome
        
    def deposito(self, quantia):
        if quantia <= 0:
            print('Insira uma quantia positiva para deposito')
        else: self.saldo += quantia
    
    def saque(self, quantia):
        if quantia <= 0:
            print('Insira uma quantia positiva para saque')
        else: self.saldo -= quantia
        
    def validacao(self):
        try:
            if self.numero_da_conta: return True
        except AttributeError: return False
            
        
conta_joao = ContaCorrente('abcd', 'Joao')
print(f'A conta do joao é valida?: {conta_joao.validacao()}')
conta_manuel = ContaCorrente('0001', 'Manuel')
print(f'A conta do manuel é valida?: {conta_manuel.validacao()}')
conta_manuel.deposito(500)
