"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de
palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador
poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""

resposta = input('Digite a Palavra: ').upper()

conjunto_palavra = set(resposta)
conjunto_letras = set()

erros = 0
while True:
    letra = input('Digite uma Letra: ').upper()

    if letra not in conjunto_palavra:
        erros += 1
        if erros <= 6:
            print(f'Você errou pela {erros}ª vez. Tente de novo!')
            continue
        break

    if letra in conjunto_palavra: conjunto_letras.add(letra)

    palavra = ''
    for letra in resposta:
        if letra in conjunto_letras: palavra += letra
        else: palavra += '_'

    print(f'A palavra é {palavra}')
    print(f'As Letras já digitadas foram {conjunto_letras}')

    if conjunto_palavra.issubset(conjunto_letras): break

if erros <= 6: print('Você Ganhou, Parabéns')
else: print('Infelismente você perdeu, melhor sorte na proxima =)')

#alteracao
