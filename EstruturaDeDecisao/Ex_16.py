#%% 16 - Equação Segundo Grau

"""
Faça um programa que calcule as raízes de uma equação do segundo grau, 
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e 
fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do 
segundo grau e o programa não deve fazer pedir os demais valores, 
sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. 
Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz 
real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao 
usuário;
"""   

a0 = float(input('Insira o valor de a: '))
b0 = float(input('Insira o valor de b: '))
c0 = float(input('Insira o valor de c: '))

def calcularbascarareal(a,b,c):
    
    if a == 0:
        print('a não pode ser igual a 0')
        return 
    
    delta = (b**2 - 4*a*c)
    
    if delta < 0:
        print('Delta <0 portanto, não possui raizes reais')
        return
    elif delta == 0:
        print('O Resultado possui apenas uma raiz real')
        x_real = (-b)/2*a
        print(f'O Valor de x é igual a: {x_real}')
        return
        
    x1 = (-b + delta**(0.5))/2*a
    x2 = (-b - delta**(0.5))/2*a
    
    print(f'O valor das raizes é igual a {x1} e {x2}')
    
calcularbascarareal(a0, b0, c0)
