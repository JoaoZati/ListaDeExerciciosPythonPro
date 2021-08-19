#%% 14 - Aumentar Salario

"""
Aprimore a classe do exercício anterior para adicionar o método 
aumentarSalario (porcentualDeAumento) que aumente o salário do 
funcionário em uma certa porcentagem.

Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
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
        
    def aumentar_salario(self, porcentagem_aumento: float):
        if not self.conta: 
            print('Conta Invalida')
            return
        
        try: i = float(porcentagem_aumento / 100)
        except ValueError: 
            print('Informar um numero float')
            return
        
        self.salario *= (1+i)
        
harry = Funcionario("Harry",25000)
harry.aumentar_salario(10)
