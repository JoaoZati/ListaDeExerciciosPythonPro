#%% 19 - Melhor sistema Operacional

"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte 
enquete feita a um grande quantidade de organizações:
    
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da 
enquete e informe ao final o resultado da mesma. O programa deverá ler 
os valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num 
vetor. Após os dados terem sido completamente informados, o programa 
deverá calcular a percentual de cada um dos concorrentes e informar o 
vencedor da enquete. O formato da saída foi dado pela empresa, e é o 
seguinte:
    
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, 
correspondendo a 40% dos votos.
"""

array_sistemas = ['Windows Server',
'Unix',                     
'Linux',                    
'Netware',                   
'Mac OS',                   
'Outro']

def inserir_voto_sistema():
    while True:
        try:
            numero = int(input("Número do sistema de 1 a 6 (0=fim): "))
            if not 0 <= numero <= 6:
                print('Informe um valor entre 1 e 6 ou 0 para sair!')
                continue
            return numero
        except ValueError:
            print('Informe um numero inteiro')
  
numero_votos = 6
array_contagem = [0]*numero_votos

while True:
    voto = inserir_voto_sistema() 
    if voto == 0: break
    
    array_contagem[voto-1] += 1

soma_votos = sum(array_contagem)

print('Sistema Operacional    Votos    %')
print('-------------------    -----    ---')
for i in range(len(array_contagem)):
    media = round((array_contagem[i] / soma_votos) * 100)
    print(f'{array_sistemas[i]}           {array_contagem[i]}    {media}%') 

print('Total: {soma_votos}')
