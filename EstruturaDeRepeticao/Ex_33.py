#%% 33 - Medidor temperatura

"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver 
um programa que leia as um conjunto indeterminado de temperaturas, e 
informe ao final a menor e a maior temperaturas informadas, bem como a 
média das temperaturas.
"""

def printsnatela(media, maior, menor, n, temp):
    print(f'A media das temperaturas é: {media}')
    print(f'A maior das temperaturas informadas é: {maior}')
    if n == 1:
        print(f'A menor das temperaturas informadas é: {temp}')
        return
    print(f'A menor das temperaturas informadas é: {menor}')
    
def DesejaParar():
    parar = input('Se dejesa parar digite "s", se dejesa continuar tecle qualquer tecla: ').upper()
    if parar == 'S':
        return True
        
temp_0 = 0
soma = 0
n = 0
while True:
    try:
        n += 1
        temp = float(input(f'Insira o valor da temperatura {n}: '))
        soma += temp
        media = soma/n
        maior = max(temp_0, temp)
        menor = min(temp_0, temp)
        temp_0 = temp
        printsnatela(media, maior, menor, n, temp)
        if DesejaParar():
            break
    except ValueError:
        print('Favor inserir apenas numeros')
