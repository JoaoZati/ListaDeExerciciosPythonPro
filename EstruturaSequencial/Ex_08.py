#%% 08 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora =  float(input('Digite um valor do salario por hora R$: '))
horas_trabalhadas =  float(input('Digite um valor das horas trabalhadas: '))

salario_mensal = salario_hora*horas_trabalhadas

print(f'O salário mensal é igual a: R$ {salario_mensal}')
