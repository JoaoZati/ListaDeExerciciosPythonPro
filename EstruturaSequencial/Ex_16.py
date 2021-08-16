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
    
