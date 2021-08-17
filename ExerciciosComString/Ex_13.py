#%% 13 - Jogo da palavra embaralhada

"""
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha 
que adivinhar uma palavra que será mostrada com as letras embaralhadas. 
O programa terá uma lista de palavras lidas de um arquivo texto e 
escolherá uma aleatoriamente. O jogador terá seis tentativas para 
adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, 
informando se o usuário ganhou ou perdeu o jogo.
"""

palavra = 'DevPro'.upper()

print('Jogo da Forca')
print('Descubra a palavra')

print('A palavra é: ', end='')
for letra in palavra:
    print(f'_', end = ' ')
    
conjunto_letras_palavras = set(palavra)
conjunto_letra_digitadas = set()
erros = 0
    
print()
print()

while (not conjunto_letras_palavras.issubset(conjunto_letra_digitadas)) and erros < 7:
    letra_digitada = input('Digite uma letra: ').upper()
    conjunto_letra_digitadas.add(letra_digitada)
    if letra_digitada in conjunto_letras_palavras:
        print('A palavra é: ', end='')
        for letra in palavra:
            if letra in conjunto_letra_digitadas: print(letra, end = ' ')
            else: print(f'_', end = ' ')
    else: 
        erros += 1
        print(f'-> Erro {erros} de 6. Tente de novo')
            
    print('Letras já Digitadas: ', conjunto_letra_digitadas)

if erros < 7: print('Parabens Você ganhou')
else: print('Você Perdeu')
