#%% 17 - Fazenda de Bichinhos

"""
Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e 
mantendo o controle deles através de uma lista. Imite o funcionamento 
do programa básico, mas ao invés de exigis que o usuário tome conta de 
um único bichinho, exija que ele tome conta da fazenda inteira. Cada 
opção do menu deveria permitir que o usuário executasse uma ação para 
todos os bichinhos (alimentar todos os bichinhos, brincar com todos os 
bichinhos, ou ouvir a todos os bichinhos). Para 
tornar o programa mais interessante, dê para cada bichinho um nivel 
inicial aleatório de fome e tédio.
"""

from random import randint

class BichinhoVirtual:
    def __init__(self, nome: str, fome = 0, saude = 100, idade = 1):
        try: int(fome), int(saude), int(idade)
        except ValueError: 
            self.nome, self.fome, self.saude, self.idade = nome, 0, 100, 1
            self.humor = self.saude - self.fome - self.idade
            return
        
        self.nome, self.fome, self.saude, self.idade = nome, fome, saude, idade
        self.humor = self.saude - self.fome - self.idade
        self.humor_brincadeiras = 0
        self.vivo = True
        self.brincadeira = False
        
    def _ajustar_humor(self):
        self.humor = self.saude - self.fome - self.idade + self.humor_brincadeiras
        
    def alimentar(self):
        if not self.vivo: return
        
        if self.fome <=20:
            self.fome = 0
            return
        
        self.fome -= 30
        self._ajustar_humor()
        
    def brincar(self):
        if not self.vivo: return
        
        self.humor_brincadeiras += 50
        self.brincadeira = True
        self._ajustar_humor()
        
    def cuidar(self):
        if not self.vivo: return

        self.saude += 20
        self._ajustar_humor()
        
    def envelhecer(self):
        if not self.vivo: return
        
        self.idade += 1
        self._ajustar_humor()
        
    def adoecer(self):
        if not self.vivo: return
        
        random = randint(0, 10)
        if 7 < random: self.saude -= 30

        self._ajustar_humor()

    def mais_fome(self):
        if not self.vivo: return
        
        self.fome += 10
        self._ajustar_humor()
    
    def tedio(self):
        if not self.vivo: return
        
        random = randint(0, 10)
        if 7 < random: self.humor -= 20
        
        if not self.brincadeira: self.humor -= 10
        self.brincadeira = False

        self._ajustar_humor()
        
    def _morrer(self):
        if not self.vivo: return
        
        if self.fome > 100 or self.humor <= 0 or self.saude <= 0: 
            self.vivo = False
            self.humor, self.saude, self.fome, self.idade = [0]*4
        
#dava para adicionar def morrer

numero_fazenda = 10

array_fazenda = [BichinhoVirtual(f'Bichinho {i+1}', randint(0, 50), randint(60, 150), randint(1, 20)) \
                 for i in range(numero_fazenda)]
 
print('''##################################################
Bem bindo ao Fazenda Bichinho Virtual:
##################################################
Você cuidara de uma fazenda de Bichinhos.
Cada Bichinho possui, saúde, fome, idade e Humor.
Seu objetivo é ter a maior soma de humor possivel.

O humor aumenta com a saude de seu bichinho.
E diminui com a fome e idade de seu bichinho.
####################################################
A cada rodada você poderá escolher entre Três opções:
    
1 - Você podera cuidar da sua fazenda, aumentando a saúde em 20 pontos de seus bichinhos
2 - Você podera alimentar sua fazenda, diminuindo a fome em 20 pontos.
3 - Você podera brincar com sua fazenda, aumentando o humor em 50 pontos
########################################################

Lembrando que a cada rodada seus bichinhos:
-Envelhecem 1 ponto.
-Crescem a fome em 5 pontos.
-Tem 20% de chance de adoecer com -20 de saúde
-Tem 20% de change de ficarem irratados diminuindo em -20 de Humor
-Cada rodada que você não brinca aumenta o tédio diminuindo em -10 de Humor
#########################################################

Ao final de cada rodada será mostrado:
A quantidade de bichinhos vivos.
A media de humor, saude, fome e idade

##########################################################

Caso: Fome > 100, Humor = 0 ou Saude = 0. Seu bichinho morrerá e você não ganhara mais humor com ele

O jogo seŕa finalizado quando:
1 - todos os seus bichinhos tem que estiverem mortos.
2 - você digitar 0 em escolher alterativa.

Seu resultado final será a soma de humor dos bichinhos.
##########################################################
Boa Sorte!
##########################################################
''')  
    

def inserir_comando():
    while True:
        comando = input('Digite o comando (1-Cuidar, 2-Alimentar, 3-Brincar e 0-Finalizar): ')
        if comando not in ['0', '1', '2', '3']: continue
        return comando
       
def metricas_fazendas(array_fazenda):
    soma_fome, soma_humor, soma_idade, soma_saude, soma_vivos = [0]*5
    for bichinho in array_fazenda:
        soma_fome += bichinho.fome        
        soma_humor += bichinho.humor
        soma_idade += bichinho.idade
        soma_saude += bichinho.saude
        if bichinho.vivo: soma_vivos += 1
    
    media_fome = soma_fome/len(array_fazenda)
    media_humor = soma_humor/len(array_fazenda)
    media_idade = soma_idade/len(array_fazenda)
    media_saude = soma_saude/len(array_fazenda)
    
    return [media_fome, media_humor, media_idade, media_saude, soma_vivos]

while True:
    array_metricas = metricas_fazendas(array_fazenda)
    print(f'Numero Bichinhos Vivos: {array_metricas[4]}, '
          f'Media Fome: {array_metricas[0]:.2f}, '
          f'Media Idade: {array_metricas[2]:.2f}, '
          f'Media Saude: {array_metricas[3]:.2f}')
    print(f'Media Humor: {array_metricas[1]:.2f}')
    
    if array_metricas[4] == 0: break
    
    comando = inserir_comando()
    if comando == '0': break

    if comando == '1': [bichinho.cuidar() for bichinho in array_fazenda]
    if comando == '2': [bichinho.alimentar() for bichinho in array_fazenda]
    if comando == '3': [bichinho.brincar() for bichinho in array_fazenda]
        
    for bichinho in array_fazenda: #pass
        bichinho._morrer()
        bichinho.adoecer()
        bichinho.envelhecer()
        bichinho.mais_fome()
        bichinho.tedio()
    
if not array_metricas[1]: print('Ops você deixou os bichinhos morrerem =/ sua média foi 0')
else: print(f'Parabéns! Seu Resultado final foi de Media Humor: {array_metricas[1]:.2f}')
