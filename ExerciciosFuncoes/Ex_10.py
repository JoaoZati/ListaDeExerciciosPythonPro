#%% 10 Jogo de Craps

"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O 
jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na 
primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se 
você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e 
você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,
este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até 
tirar este número novamente. Você perde, no entanto, se tirar um 7 
antes de tirar este Ponto novamente.
"""

array_dado = [i for i in range(1,7)]
array_dados = [i for i in range(2,13)]
array_natural = [7, 11]
array_craps = [2, 3, 12]
array_pontos = [4, 5, 6, 8, 9, 10]

def input_numero_dado(array):
    while True:
        try:
            num = int(input('Insira um numero inteiro, positivo: '))
            if num not in array:
                print(f'O numeo tem que ser estar entre {array}')
                continue
            return num
        except ValueError:
            print('Favor inseir um numero inteiro')
            
def jogo_de_craps():
    i = 0
    while True:
        dado_1 = input_numero_dado(array_dado)
        dado_2 = input_numero_dado(array_dado)
        soma = dado_1 + dado_2
        if i == 0:
            if soma in array_natural: return True
            elif soma in array_craps: return False
            ponto = soma
            print(f'Seu ponto é {ponto}')
            i += 1
            continue
        print(f'Sua soma é de {soma}')
        if soma == 7: return False
        if soma == ponto:
            return True
        
if jogo_de_craps(): print('Você foi o vencedor!')
else: print('Você Perdeu')
