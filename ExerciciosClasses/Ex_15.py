#%% 15 - Classe Bichinho vitural ++:
    
"""
Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, 
permitindo que o usuário especifique quanto de comida ele fornece ao 
bichinho e por quanto tempo ele brinca com o bichinho. Faça com que 
estes valores afetem quão rapidamente os níveis de fome e tédio caem.
"""

class BichinhoVirtual:
    def __init__(self, nome: str, fome = 0, saude = 100, idade = 1):
        try: int(fome), int(saude), int(idade)
        except ValueError: 
            self.nome, self.fome, self.saude, self.idade = nome, 0, 100, 1
            self.humor = self.saude - self.fome - self.idade
            return
        
        self.nome, self.fome, self.saude, self.idade = nome, fome, saude, idade
        self.humor = self.saude - self.fome - self.idade
        
        
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
        
jorgin = BichinhoVirtual('Jorgin', fome = 20, saude = 100, idade = 5)
jorgin.alimentar(-5)
jorgin.alimentar(5)
jorgin.brincar(-5)
jorgin.brincar(5)
