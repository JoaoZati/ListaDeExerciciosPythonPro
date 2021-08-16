#%% 11 - Organizações tabajara
"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus 
colaboradores e lhe contraram para desenvolver o programa que calculará 
os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
-salários até R$ 280,00 (incluindo) : aumento de 20%
-salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-o salário antes do reajuste;
-o percentual de aumento aplicado;
-o valor do aumento;
-o novo salário, após o aumento.
"""

salario_antigo = float(input('Insira o salário do colaborador: '))

tetominimo = [280,700,1500]
aumentos = [0.2,0.15,0.1]

aumento = 0.05
for i in range(len(tetominimo)):
    if salario_antigo < tetominimo[i]:
        aumento = aumentos[i]
        break

porcentagem_aumento = aumento*100    
valor_aumento = salario_antigo * aumento
novo_salario = salario_antigo + valor_aumento


print(f"""
-o salário antes do reajuste; R$ {salario_antigo}
-o percentual de aumento aplicado; {porcentagem_aumento} %
-o valor do aumento; R$ {valor_aumento}
-o novo salário, após o aumento. R$ {novo_salario}
      """)
