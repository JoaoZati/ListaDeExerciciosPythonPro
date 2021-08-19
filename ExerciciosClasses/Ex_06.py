#%% 06 - Classe TV

"""
Classe TV: Faça um programa que simule um televisor criando-o como um 
objeto. O usuário deve ser capaz de informar o número do canal e 
aumentar ou diminuir o volume. Certifique-se de que o número do canal e 
o nível do volume permanecem dentro de faixas válidas.
"""

class TV:
    def __init__(self, ligado = False, canal = 0, volume = 0):
        self.ligado = ligado
        if ligado: self.canal, self.volume, self.volume_memoria = canal, volume, volume
        else: 
            self.canal, self.volume = canal, 0
            self.volume_memoria = volume
        
    def ligar(self):
        self.ligado = True
        self.volume = self.volume_memoria
        
    def desligar(self):
        self.ligado = True
        self.volume = 0
        
    def trocar_canal(self, canal: int):
        if not self.ligado: return
        
        try: int(canal)
        except ValueError: return 
            
        self.canal = canal
        
    def modificar_volume(self, volume: int):
        if not self.ligado: return
        
        try: int(volume)
        except ValueError: return 
            
        self.volume += volume
        self.volume_memoria = self.volume
        
tv_lg = TV()
tv_lg.trocar_canal(12)
tv_lg.modificar_volume(5)
tv_lg.ligar()
tv_lg.trocar_canal(12)
tv_lg.modificar_volume(5)
tv_lg.desligar()
tv_lg.ligar()
