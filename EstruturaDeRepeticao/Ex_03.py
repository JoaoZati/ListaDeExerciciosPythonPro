#%% 03 - Faça um programa que leia e valide as seguintes informações:
    
"""
Faça um programa que leia e valide as seguintes informações:
-Nome: maior que 3 caracteres;
-Idade: entre 0 e 150;
-Salário: maior que zero;
-Sexo: 'f' ou 'm';
-Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    try:
        nome_3c = input('Digite seu nome (com mais que 3 caractéres): ')
        idade = int(input('Digite a sua idade (entre 0 a 150): '))
        salario = int(input('Digite o seu salário (mair que 0): '))
        sexo = input('Digite seu sexo ("f" ou "m"): ').lower()
        estado_civil = input('Digite seu estado civil ("s", "c", "v", "d"): ').lower()
    except ValueError:
        print('Favor inserir numeros quando solicitado')
    else:
        if len(nome_3c) <= 3:
            print('Nome tem que ter maisde 3 caractéres')
        elif 0 > idade > 150:
            print('A idade tem que ter de 0 a 150')
        elif salario <0 :
            print('O salario tem que ser maior que 0')
        elif sexo not in ['f', 'm']:
            print('Sexo tem que ser "f" ou "m"')
        elif estado_civil not in ['s', 'c', 'v', 'd']:
            print('Sexo tem que ser "f" ou "m"')
        else:
            print('tudo ok, informações cadastradas')
            break
