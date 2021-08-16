#%% 15 - Exemplo Renzo

"""
Faça um programa que leia um número indeterminado de valores, 
correspondentes a notas, encerrando a entrada de dados quando for 
informado um valor igual a -1 (que não deve ser armazenado).
 
Após esta entrada de dados, faça:
    
-Mostre a quantidade de valores que foram lidos;
-Exiba todos os valores na ordem em que foram informados, um ao lado do 
outro;
-Exiba todos os valores na ordem inversa à que foram informados, um 
abaixo do outro;
-Calcule e mostre a soma dos valores;
-Calcule e mostre a média dos valores;
-Calcule e mostre a quantidade de valores acima da média calculada;
-Calcule e mostre a quantidade de valores abaixo de sete;
-Encerre o programa com uma mensagem;
"""

notas = []
while True:
    entrada = input('Digite um numero: ')
    if entrada == '-1': break
    notas.append(float(entrada))

tamanho = len(notas)
print(f'foram lidas {tamanho} notas')

print(', '.join([str(nota) for nota in notas]))

notas.reverse()
for nota in notas: print(f'{nota}')

soma = sum(notas)
print(f'Soma das notas é: {soma}')

media = soma / tamanho
print(f'Media das notas é: {soma / tamanho}')

print('Notas acima da media: ')
print(' '.join([str(nota) for nota in notas if nota > media]))

print('Notas abaixo da media: ')
print(' '.join([str(nota) for nota in notas if nota < media]))

print('Encerrado o programa')
