#%% 23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento

numero_imp = float(input('Digite um numero: '))

if numero_imp == round(numero_imp):
    print('Numero inteiro')
else:
    print('Numero fracionário')
