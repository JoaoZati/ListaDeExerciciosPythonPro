#%% 05 - Vetores par e impar

"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor 
impar. Imprima os três vetores.
"""

def input_numero_int(menssagem):
    while True:
        try:
            num = int(input(menssagem))
            return num
        except ValueError:
            print('Favor inseir um numero inteiro')

def input_vetor_int(tamanho, menssagem):
    vetor = []
    for i in range(tamanho):
        numero = input_numero_int(menssagem + f'{i+1}: ')
        vetor.append(numero)
    return vetor

vetor = input_vetor_int(20, 'Insira 20 vetores, vetor ')

vetor_par = []
vetor_impar = []
for i in vetor:
    if i%2 == 0:
        vetor_par.append(i)
        continue
    vetor_impar.append(i)
    
print(f"""
Vetor = {vetor}
Vetor par = {vetor_par}
Vetor Impar = {vetor_impar}
      """)
