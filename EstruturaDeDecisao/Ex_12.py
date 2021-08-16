  #%% 12 - Calculo folha de pagamento

"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que 
os descontos são do Imposto de Renda, que depende do salário bruto 
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde 
a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de 
horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%

Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as 
informações, dispostas conforme o exemplo abaixo. No exemplo o valor da 
hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
        
"""

valor_hora = float(input('Insira valor hora: '))
horas_trab = float(input('Insira horas trabalhadas: '))
salario_antigo = valor_hora*horas_trab

imposto_FGTS = 0.11
imposto_INSS = 0.1

tetos_fgts = [900,1500,2500]
aumentos = [0,0.05,0.1]

imposto_IR = 0.2
for i in range(len(tetos_fgts)):
    if salario_antigo < tetos_fgts[i]:
        imposto_IR = aumentos[i]
        break

desconto_FGTS = imposto_FGTS*salario_antigo
desconto_INSS = imposto_INSS*salario_antigo
desconto_IR = imposto_IR*salario_antigo

total_descontos = desconto_INSS + desconto_IR
salario_liquido = salario_antigo - total_descontos

porc_FGTS = imposto_FGTS*100
porc_INSS = imposto_INSS*100
porc_IR = imposto_IR*100


print(f"""
        Salário Bruto: ({valor_hora} * {horas_trab})        : R$ {salario_antigo}
        (-) IR ({porc_IR}%)                     : R$   {desconto_IR} 
        (-) INSS ( {porc_INSS}%)                 : R$  {desconto_INSS}
        FGTS ({porc_FGTS}%)                      : R$  {desconto_FGTS}
        Total de descontos              : R$  {total_descontos}
        Salário Liquido                 : R$  {salario_liquido}
      """)
