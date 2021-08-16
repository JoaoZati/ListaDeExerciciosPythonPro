#%% 44 - Eleição Presidencial

"""
Em uma eleição presidencial existem quatro candidatos. Os votos são 
informados por meio de código. Os códigos utilizados são:
    
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
-O total de votos para cada candidato;
-O total de votos nulos;
-O total de votos em branco;
-A percentagem de votos nulos sobre o total de votos;
-A percentagem de votos em branco sobre o total de votos. Para 
finalizar o conjunto de votos tem-se o valor zero.
"""

dic_votos = {1: 'João',
             2: "José",
             3: 'Gabriel',
             4: 'Renato',
             5: 'Nulo',
             6: 'Branco'}

dic_codigo_soma = {1: 0,
                   2: 0,
                   3: 0,
                   4: 0,
                   5: 0,
                   6: 0,}

def imputcodigo_urna(menssagem, dicionario):
    while True:
        try:
            inp = int(input(menssagem))
            if inp not in dicionario.keys() and inp != 0:
                print('O codigo não consta na urna')
                continue
            return inp
        except ValueError:
            print('Você deve fornecer apenas numeros')
            
menssagem = f"""Para contar o voto Digite:
{dic_votos}
Para sair digite 0: """

def contagem_de_votos(codigo, dic_soma):
    for key in dic_soma.keys():
        if codigo == key:
            dic_soma[key] += 1

while True:
    codigo = imputcodigo_urna(menssagem, dic_votos)
    if codigo == 0:
        break
    
    contagem_de_votos(codigo, dic_codigo_soma)

total_votos = 0
for key, value in dic_codigo_soma.items():
    total_votos += value
    
print('')
print('O Resultado da votação é: ')
for key, value in dic_codigo_soma.items():
    if value == 1:
        print(f'Digito {key}, {dic_votos[key]}: {value} voto')
        continue
    print(f'Digito {key}, {dic_votos[key]}: {value} votos')

porc_nulos = round((dic_codigo_soma[5] / total_votos) * 100, 1) 
porc_brancos = round((dic_codigo_soma[6] / total_votos) * 100, 2)

print(f'A porcentagem de votos nulos é {porc_nulos}%')
print(f'A porcentagem de votos brancos é {porc_brancos}%')
