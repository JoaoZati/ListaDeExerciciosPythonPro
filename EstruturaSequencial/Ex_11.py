#%% 11 - 2 numeros inteiros

"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
a - o produto do dobro do primeiro com metade do segundo .
b - a soma do triplo do primeiro com o terceiro.
c - o terceiro elevado ao cubo.
"""

numint_1 = int(input('Digite primeiro número inteiro: '))
numint_2 = int(input('Digite segundo número inteiro: '))
num_real = float(input('Digite um número real: '))

questao_a = (numint_1*2)*(numint_2/2)
questao_b = (numint_1*3)+num_real
questao_c = (num_real**3)

print(f"""
questão a: {questao_a}
questão b: {questao_b}
questão c: {questao_c}
              """)
