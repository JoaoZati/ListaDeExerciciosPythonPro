
"""
Faça um programa que use a função valorPagamento para determinar o valor 
a ser pago por uma prestação de uma conta. O programa deverá solicitar 
ao usuário o valor da prestação e o número de dias em atraso e passar 
estes valores para a função valorPagamento, que calculará o valor a ser 
pago e devolverá este valor ao programa que a chamou. O programa deverá 
então exibir o valor a ser pago na tela. Após a execução o programa 
deverá voltar a pedir outro valor de prestação e assim continuar até que 
seja informado um valor igual a zero para a prestação. Neste momento o 
programa deverá ser encerrado, exibindo o relatório do dia, que conterá 
a quantidade e o valor total de prestações pagas no dia. O cálculo do 
valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, 
cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, 
mais 0,1% de juros por dia de atraso.
"""

valor_conta = 1000
dias_atraso = 30

#parar 0
def inserir_numero_sistema(menssagem):
    while True:
        try:
            numero = float(input(menssagem))
            if numero < 0:
                print('Informar numero maior igual a 0')
                continue
            return numero
        except ValueError:
            print('Informe um numero inteiro')

def valorPagamento(valor, dias):
    if dias == 0: return valor
    return round(valor * (1 + 0.03)**(1 + 0.01*dias), 2)

print(valorPagamento(valor_conta, dias_atraso))

while True:
    valor_conta = inserir_numero_sistema('Favor inserir valor da conta (0 = sair): ')
    if valor_conta == 0: break
    dias_atraso = inserir_numero_sistema('Favor inserir dias de atraso: ')
    valor_pagar = valorPagamento(valor_conta, dias_atraso)
    
    print(f'Valor a pagar é de: R$ {valor_pagar}')
