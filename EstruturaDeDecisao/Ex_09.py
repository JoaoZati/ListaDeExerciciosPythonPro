#%% 09 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero_1 = float(input('Insira o preço do primeiro produto: '))
numero_2 = float(input('Insira o preço do segundo produto: '))
numero_3 = float(input('Insira o preço do terceiro produto: '))

lista_num = [numero_1, numero_2, numero_3]
nova_lista = []

menor = numero_1
tamanho = len(lista_num)
           
for i in list(range(tamanho)):
    for num in lista_num:
        if num > menor:
            menor = num
            
    nova_lista.append(menor)
    lista_num.remove(menor)
    
    if len(lista_num) != 0:
        menor = lista_num[0]
        
print(f' A ordem dos número decrescente é: {nova_lista}')
