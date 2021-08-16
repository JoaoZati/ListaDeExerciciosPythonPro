#%% 04 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Insira uma letra: ').upper()

if len(letra) != 1:
    print('Você não digitou uma letra')
elif letra == 'A' or letra == "E" or letra == "I" or letra == 'O' or letra == "U":
    print('A letra é uma vogal')
else:
    print('A letra é uma consoante ou um caractére')
