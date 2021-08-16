#%% 06 - imprime 1 a 20

"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do 
outro. Depois modifique o programa para que ele mostre os números um ao 
lado do outro.
"""

numero = 20

for i in range(1,numero+1):
    print(i)
    
print("""
      
      """)
      
string_lado = ''

for i in range(1,numero+1):
    string_lado += f'{i} '
    
print(string_lado)
