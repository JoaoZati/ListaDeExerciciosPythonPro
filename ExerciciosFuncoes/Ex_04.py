#%% 04 - Positivo ou negativo

"""
Faça um programa, com uma função que necessite de um argumento. A função 
retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, 
se seu argumento for zero ou negativo.
"""

def inserir_numero_sistema():
    while True:
        try:
            numero = float(input("Informe um numero: "))
            return numero
        except ValueError:
            print('Informe um numero inteiro')
            
def verificar_se_eh_positivo(n):
    if n >= 0: print('P')
    else: print('N')
    
num = inserir_numero_sistema()
verificar_se_eh_positivo(num)
