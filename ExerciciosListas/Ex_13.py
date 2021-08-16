#%% 13 - Temperatura a cada mes

"""
Faça um programa que receba a temperatura média de cada mês do ano e 
armazene-as em uma lista. Após isto, calcule a média anual das 
temperaturas e mostre todas as temperaturas acima da média anual, e em 
que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 
2 – Fevereiro, . . . ).
"""

def input_numero_float(menssagem):
    while True:
        try:
            num = float(input(menssagem))
            return num
        except ValueError:
            print('Favor inseir um numero')

vetor_nomes = ['1-Janeiro',
            '2-Fevereiro',
            '3-Março',
            '4-Abril',
            '5-Maio',
            '6-Junho',
            '7-Julho',
            '8-Agosto',
            '9-Setembro',
            '10-Outubro',
            '11-Novembro',
            '12-Dezembro'] 

vetor_temperaturas = []
for mes in vetor_nomes: 
    temp = input_numero_float(f'Insira a temperatura de {mes}: ')
    vetor_temperaturas.append(temp)

elementos = len(vetor_temperaturas)
media_temperatura = sum(vetor_temperaturas) / elementos
vetor_temp_maior = []
for i in range(elementos):
    if vetor_temperaturas[i] >= media_temperatura: vetor_temp_maior.append(i+1)

print(', '.join([str(vetor_nomes[i]) for i in range(len(vetor_nomes)) if i+1 in vetor_temp_maior]))
