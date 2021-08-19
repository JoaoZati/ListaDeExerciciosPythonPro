#%% 08 - Classe Macaco

"""
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome 
e bucho (estomago) e pelo menos os métodos comer(), verBucho() e 
digerir(). Faça um programa ou teste interativamente, criando pelo menos 
dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e 
verificando o conteúdo do estomago a cada refeição. Experimente fazer 
com que um macaco coma o outro. É possível criar um macaco canibal?
"""

class Macaco:
    def __init__(self, nome: str, bucho = []):
        self.nome = nome
        if (type(bucho) == list): self.bucho = bucho
        else: self.bucho = []
    
    def comer(self, comida):
        self.bucho.append(comida)        
    
    def ver_bucho(self):
        print(self.bucho)
        
    def digerir(self, comida):
        if comida not in self.bucho: return
        else: self.bucho.remove(comida)
        
macaco1 = Macaco('Jorge', 8)
macaco2 = Macaco('Gabriel', ['abacate', 'uva'])

macaco1.comer(macaco2)
macaco1.ver_bucho()

macaco1.bucho[0].digerir('uva')
macaco1.bucho[0].ver_bucho()
macaco2.ver_bucho()
