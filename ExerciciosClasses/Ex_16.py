#%% 16 - Porta Escondida

"""
Crie uma "porta escondida" no programa do programa do bichinho virtual 
que mostre os valores exatos dos atributos do objeto. Consiga isto 
mostrando o objeto quando uma opção secreta, não listada no menu, for 
informada na escolha do usuário. Dica: acrescente um método especial 
str() à classe Bichinho.
"""

class BichinhoVirtual:
    def _opcao_secreta(self):
        if self.mostrar == 'S':
            print(f'nome: {self.nome}, fome: {self.fome}, saude: {self.saude}, idade: {self.idade}, humor: {self.humor}')
    
    def __init__(self, nome: str, fome, saude, idade, mostrar = 'N'):
        try: int(fome), int(saude), int(idade)
        except ValueError: 
            self.nome, self.fome, self.saude, self.idade = nome, 0, 100, 1
            self.humor = self.saude - self.fome - self.idade
            return
        
        self.nome, self.fome, self.saude, self.idade = nome, fome, saude, idade
        self.humor = self.saude - self.fome - self.idade
        
        self.mostrar = mostrar.upper()
        self._opcao_secreta()
        
    def alterar_nome(self, nome: str):
        self.nome = nome
        
    def alterar_fome(self, fome: int):
        try: int(fome)
        except ValueError: return
        
        self.fome += fome
        self.humor = self.saude - self.fome - self.idade
    
    def alterar_idade(self, idade: int):
        try: int(idade)
        except ValueError: return
        
        if idade < 0: return
        
        self.idade += idade
        self.humor = self.saude - self.fome - self.idade
        
    def alterar_saude(self, saude: int):
        try: int(saude)
        except ValueError: return
        
        self.saude += saude
        self.humor = self.saude - self.fome - self.idade
        
    def alimentar(self, alimento: int):
        try: int(alimento)
        except ValueError: return
        
        if alimento <= 0: return
        
        self.fome -= alimento
        self.humor = self.saude - self.fome - self.idade
        
    def brincar(self, tempo: int):
        
        try: int(tempo)
        except ValueError: return
        
        if tempo <= 0: return
        
        self.humor += tempo
        
piquinic = BichinhoVirtual('Piquinic', 10, 120, 2, mostrar = 's')
