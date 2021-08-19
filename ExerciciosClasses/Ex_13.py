#%% 13 - Classe Funcionario

"""
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um 
nome (um string) e um salário(um double). Escreva um construtor com dois 
parâmetros (nome e salário) e métodos para devolver nome e salário. 
Escreva um pequeno programa que teste sua classe.
"""

class Funcionario:
    def _validar_conta(self):
        if not self.nome: self.conta = False
        
        try: self.salario = float(self.salario)
        except ValueError: 
            print('Salario tem que ser um numero conta invalida')
            self.conta = False
            return
        
        if self.salario <= 0: self.conta = False
        else: self.conta = True
        
    
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario
        
        self._validar_conta()
        
    def mostrar_salario(self):
        if self.conta: print(f'{self.salario:.2f}')
        else: print('Conta invalida') 
        
    def mostrar_nome(self):
        if self.conta: print(self.nome)
        else: print('Conta Inválida')
        
    def demissao(self):
        self.salario = 0
        self._validar_conta()
        
    def aumento(self, aumento: float):
        if self.conta: self.salario += aumento       
        else: print('Conta Inválida')
        
    def recontratacao(self, salario: float):
        self.salario = salario
        
        self._validar_conta()
        
        if self.conta: print('Conta Reativada com sucesso')
        else: print('Conta não reativada com sucesso')

joao = Funcionario('Joao', 2500)
joao.mostrar_salario()
joao.mostrar_nome()

joao.aumento(500)
joao.mostrar_salario()

joao.demissao()
print(joao.conta)
joao.mostrar_salario()

joao.recontratacao(-500)
joao.recontratacao(2500)
