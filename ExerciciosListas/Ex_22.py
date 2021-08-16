#%% 22 - Aproveitamento Mause

"""
Sua organização acaba de contratar um estagiário para trabalhar no 
Suporte de Informática, com a intenção de fazer um levantamento nas 
sucatas encontradas nesta área. A primeira tarefa dele é testar todos 
os cerca de 200 mouses que se encontram lá, testando e anotando o 
estado de cada um deles, para verificar o que se pode aproveitar deles.

Foi requisitado que você desenvolva um programa para registrar este 
levantamento. O programa deverá receber um número indeterminado de 
entradas, cada uma contendo: um número de identificação do mouse o tipo 
de defeito:
    
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; 
a.quebrado ou inutilizado Uma identificação igual a zero encerra o 
programa. Ao final o programa deverá emitir o seguinte relatório:
    
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

def inserir_int_sistema():
    while True:
        try:
            numero = int(input("Número do sistema de 1 a 4 (0=fim): "))
            if not 0 <= numero <= 4:
                print('Informe um valor entre 1 e 4 ou 0 para sair!')
                continue
            return numero
        except ValueError:
            print('Informe um numero inteiro')

array_entrada = []            
while True:
    entrada = inserir_int_sistema()
    if entrada == 0: break
    array_entrada.append(entrada)

array_mause = ['1- necessita da esfera',
               '2- necessita de limpeza',
               '3- necessita troca do cabo ou conector',
               '4- quebrado ou inutilizado']

array_inputs = [1,2,3,4]  

array_quantidades = [0]*4
for i in range(len(array_entrada)):
    for j in range(len(array_inputs)):
        if array_entrada[i] == array_inputs[j]: array_quantidades[j] += 1 

print('')        
print(f'Quantidades de mauses: {len(array_entrada)}')
print('')

print('Situação         -          Quantidade        -         Percentual')
for i in range(len(array_quantidades)):
    percentual = round(array_quantidades[i] / len(array_entrada) * 100, 2)
    print(f'{array_mause[i]}    -    {array_quantidades[i]}    -    {percentual}%')
    
