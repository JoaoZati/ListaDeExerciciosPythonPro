#%% 06 - 24 horas em 12h

"""
Faça um programa que converta da notação de 24 horas para a notação de 
12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: 
uma para fazer a conversão e uma para a saída. Registre a informação 
A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a 
função para efetuar as conversões terá um parâmetro formal para 
registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário 
repita esse cálculo para novos valores de entrada todas as vezes que 
desejar.
"""

while True:
    try:
        hora_entrada = input('Insira hora no formato 24:59 PM')
        hora_string = hora_entrada[:-3]
        hora, minuto = [int(i) for i in hora_string.split(':')]
        if not 0 <= hora <= 24 or not 0 <= minuto <= 60: print('Insira corretamente a hora no formato 24:59 PM: ')
        else: break
    except ValueError:
        print('Insira corretamente a hora no formato 24:59 PM')

def conversao_24_em_12(hora_entrada):
    hora_string = hora_entrada[:-3]
    hora, minuto = [int(i) for i in hora_string.split(':')]
    
    if hora >= 12: 
        hora -= 12
        complemento = ' PM'
    else: complemento = ' AM'
    
    return str(hora) + ':' + str(minuto) + complemento

hora_saida = conversao_24_em_12(hora_entrada)
print(hora_saida)
