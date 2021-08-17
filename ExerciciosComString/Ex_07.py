#%% 07 - Conta Espaços e Vogais 

string = input('Digite um texto: ')

array_contagem = ['A', 'E', 'I', 'O', 'U']

total_espacos = len([palavra for palavra in string if palavra == ' '])
total_vogais = len([palavra for palavra in string.upper() if palavra in array_contagem])

print(f'O total de espaços é {total_espacos}')
print(f'O total de vogais é {total_vogais}')
