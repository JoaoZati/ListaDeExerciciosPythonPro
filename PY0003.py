#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 18:42:48 2021

@author: joao

Estrutura Sequencial
>>> Desafio exercicio 17
"""

#%% 01-Faça um Programa que mostre a mensagem "Alo Mundo" na tela.

print('Alo Mundo')
type("Alo Mundo")

#%% 02 - Numero que mostra mensagem

"""
2.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""

numero = input('Digite um número: ') #Tipo string
print(f'O Numero informado foi {numero}')

#%% 03 - Faça um Programa que peça dois números e imprima a soma.
print('Soma de Dois Numeros')

numero_1 = int(input('Digite primeiro número: '))
numero_2 = int(input('Digite Segundo número: '))  #Operação de soma
#print(type(numero_1))

soma = numero_1 + numero_2
print(f'A soma dos dois números é: {soma}')

#%% 04 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

soma = 0
for i in list(range(1,5)):
    nota = float(input(f'Digite a nota {i}: '))
    soma += nota
    
media = soma/4
    
print(f'A media das notas é igual a: {media}')

#%% 05 - Faça um Programa que converta metros para centímetros.

metro_imp = float(input('Digite um valor em metros para converter em cm: '))
centrimetro_imp = metro_imp*100

print(f'O valor em cm é igual a: {centrimetro_imp}cm')

#%% 06 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio_cir = float(input('Digite um valor em metros do raio do circulo para calcular a área: '))
area_cir =  (raio_cir**2)*3.1415

print(f'O valor da área do circulo de raio {raio_cir} é igual a: {area_cir}')

#%% 07 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

aresta_quadrado =  float(input('Digite um valor da aresta: '))
area_quadrado = aresta_quadrado**2
area_quadrado_x2 = area_quadrado*2

print(f'O dobro da área do quadrado de aresta {aresta_quadrado} é igual a : {area_quadrado_x2}')

#%% 08 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora =  float(input('Digite um valor do salario por hora R$: '))
horas_trabalhadas =  float(input('Digite um valor das horas trabalhadas: '))

salario_mensal = salario_hora*horas_trabalhadas

print(f'O salário mensal é igual a: R$ {salario_mensal}')

#%% 09 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

temp_f =  float(input('Digite um valor da temperatura Fahrenheit: '))

Celsius = 5 * ((temp_f-32) / 9)

print(f'A temperatura em Celsius é igual a: {Celsius} Cº')

#%% 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temp_c =  float(input('Digite um valor da temperatura Celsius: '))
Fahrenheit = ((temp_c/5)*9)+32

print(f'A temperatura em Fahrenheit é igual a: {Fahrenheit} Cº')

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

#%% 12 - Calculo Altura
"""
Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: 
(72.7*altura) - 58
"""

altura = float(input('Digite a altura em metros: '))
peso_ideal = (72.7*altura) - 58

print(f'O peso ideial é de: {peso_ideal}')

#%% 13 - Peso Ideial Homem x Mulher

"""
Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
    
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

"""

altura = float(input('Digite a altura em metros: '))
genero = input('Insira o genero. Digite H para homem ou M para Mulher: ')

if genero != 'H' and genero != 'M':
    print('''
          Input Errado use H para Homem e M para Mulher: 
          verefique o uso de capslock ''')
        
peso_ideal_H = (72.7*altura) - 58
peso_ideal_M = (62.1*altura) - 44.7

if genero == 'H':    
    print(f'O peso ideial é de: {peso_ideal_H}')
elif genero == 'M':
    print(f'O peso ideial é de: {peso_ideal_M}')

#%% 14 - João e os peixes

"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para 
controlar o rendimento diário de seu trabalho. Toda vez que ele traz um 
peso de peixes maior que o estabelecido pelo regulamento de pesca do 
estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por 
quilo excedente. João precisa que você faça um programa que leia a 
variável peso (peso de peixes) e calcule o excesso. Gravar na variável 
excesso a quantidade de quilos além do limite e na variável multa o 
valor da multa que João deverá pagar. Imprima os dados do programa com 
as mensagens adequadas.
"""

peso_peixes = float(input('Insira o peso total da pescaria: '))

def calculoexcessodepeso(peso_p):
    excesso_peso = peso_p - 50
    
    if excesso_peso <= 0:
        print('Não ouve excesso de peso')
        return 
    
    excesso_multa = excesso_peso*4
    
    print(f'O excesso de peso foi de: {excesso_peso} Kg')
    print(f'A multa a ser paga é de: R$ {excesso_multa}')
    
calculoexcessodepeso(peso_peixes)

#%% 15 - Salario mais complexo

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de 
horas trabalhadas no mês. Calcule e mostre o total do seu salário no
referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    
-salário bruto.
-quanto pagou ao INSS.
-quanto pagou ao sindicato.
-o salário líquido.
-calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

salario_hora =  float(input('Digite um valor do salario por hora R$: '))
horas_trabalhadas =  float(input('Digite um valor das horas trabalhadas: '))

salario_bruto = salario_hora*horas_trabalhadas
Desconto_IR = salario_bruto*0.11
Desconto_INSS = salario_bruto*0.08
Desconto_Sindcato = salario_bruto*0.05

total_descontos = Desconto_INSS + Desconto_IR + Desconto_Sindcato 
salario_liquido = salario_bruto - total_descontos

print(f"""
+ Salário Bruto: R$ {salario_bruto}
- IR (11%) : R$ {Desconto_IR}
- INSS (8%) : R$ {Desconto_INSS}
- Sindicato ( 5%) : R$ {Desconto_Sindcato}
= Salário Liquido : R$ {salario_liquido}
      """)
      
#%% 16 - Problema Loja de Tintas

"""
Faça um programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada. Considere que a 
cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a 
tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao 
usuário a quantidades de latas de tinta a serem compradas e o preço 
total.
"""

area_pintada = float(input('Digite o valor em m² a ser pintada: '))

litros_usados = area_pintada/3
quantidade_latas_float = litros_usados/18

def roundup(num):
    resto = num%1
    
    if resto == 0:
        return num
    
    round_up = (num - resto) + 1
    return round_up

quantidade_latas_int = roundup(quantidade_latas_float)
valor_latas_pagar = quantidade_latas_int*80

print(f"""
      A quantidade de latas a serem compradas é de: {quantidade_latas_int} un
      O valor a ser pago é de: R$ {valor_latas_pagar}
      """)
    
#%% 17 - Problema dever de casa: loja de tintas

"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada. Considere que a 
cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a 
tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões 
de 3,6 litros, que custam R$ 25,00.
a) Informe ao usuário as quantidades de tinta a serem compradas e os 
respectivos preços em 3 situações:
b) comprar apenas latas de 18 litros;
c) comprar apenas galões de 3,6 litros;
d) misturar latas e galões, de forma que o desperdício (eu usei preço) de tinta seja 
menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
isto é, considere latas cheias.
"""
    
area_pintada_sem_folga = float(input('Digite o valor em m² a ser pintada: '))
area_pintada = area_pintada_sem_folga*1.1

litros_usados = area_pintada/6
quantidade_18_f = litros_usados/18
quantidade_36_f = litros_usados/3.6

def roundup(num):
    resto = num%1
    
    if resto == 0:
        return num
    
    round_up = (num - resto) + 1
    return round_up

def rounddown(num):
    resto = num%1
    round_down = num - resto
    return round_down
    

quantidade_latas_18 = roundup(quantidade_18_f)
valor_latas_18 = quantidade_latas_18*80

quantidade_latas_36 = roundup(quantidade_36_f)
valor_latas_36 = quantidade_latas_36*25

area = 180
def calculootimizado(area):
    litros = area/6
    qntf_18 = litros/18
    qnt_18 = int(rounddown(qntf_18))
    qnt_18_max = int(roundup(qntf_18))
    
    valor_otm = qnt_18_max*80
    latas_final_18 = qnt_18_max
    latas_final_36 = 0
    for i in list(range(qnt_18+1)):
        sobra = litros - i*18
        litros_36 = sobra/3.6
        latas_36 = roundup(litros_36)
        
        calc = i*80 + latas_36*25
        
        print(f''' 
                   quantidade litros 18l: {i}
                   quantidade litros 3,6l: {latas_36}
                   valor a pagar: R$ {calc}''')
        
        if calc < valor_otm:
            valor_otm = calc
            latas_final_18 = i
            latas_final_36 = latas_36
        
        valor_18_print = qnt_18_max*80
        
    print(f''' 
                   quantidade litros 18l: {qnt_18_max}
                   quantidade litros 3,6l: {0}
                   valor a pagar: R$ {valor_18_print}''')
            
    return valor_otm, latas_final_18, latas_final_36

valor_otimizado, quantidade_18_otm, quantidade_36_otm = calculootimizado(area_pintada)


print(f"""
      ###################################################################################
      
      A quantidade de latas a serem compradas de apenas 18l: {quantidade_latas_18} un
      O valor a ser pago com apenas latas de 18l é de: R$ {valor_latas_18}
      
      ###################################################################################
      
      A quantidade de latas a serem compradas de apenas 3.6l: {quantidade_latas_36} un
      O valor a ser pago com apenas latas de 3.6l é de: R$ {valor_latas_36}
      
      ###################################################################################
      
      As Quantidades otimizadas utilizando tando 18l e 3.6l é de:
      Quantidade de Latas de 18l: {quantidade_18_otm} un
      Quantidade de Latas de 36l: {quantidade_36_otm} un
      
      O valor final mais otimizado é de: R$ {valor_otimizado}
      
      ###################################################################################
      """)

"""
     print(f''' valor otm: {valor_otm}
                   quantidade 18: {i}
                   quantidade 3,6: {latas_36}
                   calc: {calc}''')
usei para visualizar a resolução
"""

#%% 18 - Tamanho do arquivo MB

"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps), calcule e informe o 
tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_arquivo = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a velocidade de download em Mbps: '))

tempo_segundos = tamanho_arquivo/velocidade

def rounddown_min(num):
    segundos = num%60
    minutos = (num - segundos)/60
    
    return minutos, segundos

Qt_minutos, Qt_segundos = rounddown_min(tempo_segundos)

print(f"""
Seu download demorará: 
{tempo_segundos} segundos
ou
{Qt_minutos} minutos e {Qt_segundos} segundos
      """)
      
#%% - Solução Renzo Problema 17 
import math

area_a_ser_pintada = float(input("Digite a area a ser pintada: ")) #area em metros quadrados
area_com_folga = area_a_ser_pintada*1.1

litros_por_metro = 6
litros_a_serem_usados = area_com_folga/litros_por_metro

litros_por_lata = 18
valor_por_lata = 80
numero_de_latas = math.ceil(litros_a_serem_usados/litros_por_lata)
valor_com_apenas_latas = numero_de_latas*valor_por_lata

print(f'Você devera usar {numero_de_latas} latas de 18 litros, no valor de R$ {valor_com_apenas_latas}') 

litros_por_galao = 3.6
valor_por_galao = 25
numero_de_galao = math.ceil(litros_a_serem_usados/litros_por_galao)
valor_com_apenas_galao = numero_de_galao*valor_por_galao

print(f'Você devera usar {numero_de_galao} galões de 3.6 litros, no valor de R$ {valor_com_apenas_galao}') 

#compra de tinta otimizada no valor
numero_de_latas = math.floor(litros_a_serem_usados/litros_por_lata)
valor_com_apenas_latas = numero_de_latas*valor_por_lata
litros_faltantes = litros_a_serem_usados % litros_por_lata
numero_de_galao = math.ceil(litros_faltantes/litros_por_galao)
valor_com_apenas_galao = numero_de_galao*valor_por_galao

valor_total = valor_com_apenas_latas + valor_com_apenas_galao 

print(f'Você devera usar {numero_de_latas} latas de 18 litros e {numero_de_galao} galões de 3.6 litros, no valor de R$ {valor_total}') 


