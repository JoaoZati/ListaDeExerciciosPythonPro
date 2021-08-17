"""
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário 
digitar o seu nome e em seguida mostre o nome do usuário de trás para 
frente utilizando somente letras maiúsculas. Dica: lembre−se que ao 
informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
"""

nome = input('Digite seu nome destacando maiusculas: ').upper()

nome_invertido = ''.join(reversed(nome))
nome_invertido_2 = ' '.join(reversed(nome.split()))

print(f'Nome original {nome}')
print(f'Nome original invertido {nome_invertido}')
print(f'Nome original invertido por palavras {nome_invertido_2}')
