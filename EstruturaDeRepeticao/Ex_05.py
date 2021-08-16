#%% 05 - População input usuario

"""
Altere o programa anterior permitindo ao usuário informar as populações 
e as taxas de crescimento iniciais. Valide a entrada e permita repetir a 
operação.
"""

while True:
    try:
        pop_a = int(input('Digite a população Menor A: '))
        pop_b = int(input("Digite a população Maior B: "))
        cresc_a = float(input("Digite a taxa de crescimento maior A (ex: 10%, digite 1.1): "))
        cresc_b = float(input("Digite a taxa de crescimento menor B (ex: 10%, digite 1.1): "))
    except ValueError:
        print('Favor digitar numeros inteiros em populações e reais em crescimento')
    else:
        if pop_b <= pop_a or cresc_b >= cresc_a:
            print('''
                  A população de A deve ser menor que B 
                  E a taxa de crescimento de A deve ser maior que B''')
        else:
            soma = 1
            while True:
                pop_a *= cresc_a
                pop_b *= cresc_b
                
                if pop_a >= pop_b:
                    print(f'demorou {soma} anos para igualar')
                    break
                
                soma += 1
                
            break
