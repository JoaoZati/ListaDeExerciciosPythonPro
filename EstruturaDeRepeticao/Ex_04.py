#%% 04 - Exercicio população

"""
Supondo que a população de um país A seja da ordem de 80000 habitantes 
com uma taxa anual de crescimento de 3% e que a população de B seja 
200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa 
que calcule e escreva o número de anos necessários para que a população 
do país A ultrapasse ou iguale a população do país B, mantidas as taxas 
de crescimento.
"""

pop_a = 80000
pop_b = 200000

cresc_a = 1.03
cresc_b = 1.015

x = 1
while True:
    pop_a *= cresc_a
    pop_b *= cresc_b
    
    if pop_a >= pop_b:
        print(f'demorou {x} anos para igualar')
        break
    
    x += 1
