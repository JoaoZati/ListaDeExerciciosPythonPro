#%% 35 - Primos entre 1 e N

"""
Encontrar números primos é uma tarefa difícil. Faça um programa que 
gera uma lista dos números primos existentes entre 1 e um número 
inteiro informado pelo usuário.
"""

while True:
    try:
        num_p = int(input('Insira um numero inteiro N: '))
    except ValueError:
        print('Não foi fornecido um numero inteiro')
    else:
        if num_p < 0:
            print('numero precisa ser positivo')
        else:
            break

def VerificarSeEhPrimo(num):
    count = 0
    for i in range(2, num):
        if num%i == 0:
            count += 1
    
    if count == 0:
        return True
    return False

list_primo = []
for i in range(2, num_p):
    bool_primo = VerificarSeEhPrimo(i)
    if bool_primo:
        list_primo.append(i)
        
print(f'''A lista de numeros primos entre 1 e {num_p} é:''')
for i in list_primo:
    print(i)
