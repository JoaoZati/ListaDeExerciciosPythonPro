#%% 15 - Triangulos

"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá 
informar se os valores podem ser um triângulo. Indique, caso os lados 
formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
-Três lados formam um triângulo quando a soma de quaisquer dois lados 
for maior que o terceiro;
-Triângulo Equilátero: três lados iguais;
-Triângulo Isósceles: quaisquer dois lados iguais;
-Triângulo Escaleno: três lados diferentes;

"""

lado_trian_1 = float(input('Insira o valor do primeiro lado: '))
lado_trian_2 = float(input('Insira o valor do segundo lado: '))
lado_trian_3 = float(input('Insira o valor do terceiro lado: '))

def classificartriangulo(lado_1, lado_2, lado_3):
    if lado_1 >= lado_2 + lado_3 or \
       lado_2 >= lado_1 + lado_3 or \
       lado_3 >= lado_1 + lado_2:
        print('Os valores Fornecidos não formam um triangulo')
        return
    
    if lado_1 == lado_2 and lado_1 == lado_3 and lado_2 == lado_3:
        print('Triangulo é Equilátero')
        return
    
    if lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print('Triangulo é Isóceles')
        return
    
    print('Triangulo é Escaleno')
        
classificartriangulo(lado_trian_1, lado_trian_2, lado_trian_3)
