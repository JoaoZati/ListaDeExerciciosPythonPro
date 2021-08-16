#%% 02 - Nome e senha

"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando
 a pedir as informações.
"""

while True:
    
    nome_usuario = input('Digite o nome de usuário: ')
    senha_usuario = input('Digite a senha: ')
        
    if nome_usuario != senha_usuario:
        print('Nome e senha válidos')
        continue
    break
    
    print('Sorry, o nome e a senha não podem ser a mesma: ')
