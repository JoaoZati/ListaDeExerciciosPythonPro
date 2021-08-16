#%% 26 - Candidatos

"""
Numa eleição existem três candidatos. Faça um programa que peça o número 
total de eleitores. Peça para cada eleitor votar e ao final mostrar o 
número de votos de cada candidato.
"""

while True:
    try:
        n = int(input('Insira o numero de eleitores: '))
        if n <= 0:
            print('Numero precisa ser maior que 0')
            continue
        break
    except ValueError:
        print('Não foi fornecido um numero inteiro')


numero = 0
num_1candidato = 0
num_2candidato = 0
num_3candidato = 0
while True:
    try:
        num = int(input(f'''Insira o voto do eleitor {numero + 1}
(digite 1 para o candidato 1, digite 2 para o candidato 2 ou digite 3 para o candidato 3.): '''))
        if num not in [1,2,3]:
            print('O voto tem que ser 1, 2 ou 3')
            continue
        
        if num == 1:
            num_1candidato += 1
        elif num == 2:
            num_2candidato += 1
        elif num == 3:
            num_3candidato += 1

        numero += 1
        if numero >= n:
            break
    except ValueError:
        print('Deve informar um numero inteiro')
        
num_vencedor = max(num_1candidato, num_2candidato, num_3candidato)

print(f"""
Com {num_vencedor} votos o vencedor foi:
Candidato 1: {num_1candidato}
Candidato 2: {num_2candidato}
Candidato 3: {num_3candidato}
      """)
