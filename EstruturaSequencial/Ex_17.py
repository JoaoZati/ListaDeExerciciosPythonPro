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
