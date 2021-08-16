#%% 15 - Salario mais complexo

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de 
horas trabalhadas no mês. Calcule e mostre o total do seu salário no
referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    
-salário bruto.
-quanto pagou ao INSS.
-quanto pagou ao sindicato.
-o salário líquido.
-calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

salario_hora =  float(input('Digite um valor do salario por hora R$: '))
horas_trabalhadas =  float(input('Digite um valor das horas trabalhadas: '))

salario_bruto = salario_hora*horas_trabalhadas
Desconto_IR = salario_bruto*0.11
Desconto_INSS = salario_bruto*0.08
Desconto_Sindcato = salario_bruto*0.05

total_descontos = Desconto_INSS + Desconto_IR + Desconto_Sindcato 
salario_liquido = salario_bruto - total_descontos

print(f"""
+ Salário Bruto: R$ {salario_bruto}
- IR (11%) : R$ {Desconto_IR}
- INSS (8%) : R$ {Desconto_INSS}
- Sindicato ( 5%) : R$ {Desconto_Sindcato}
= Salário Liquido : R$ {salario_liquido}
      """)
