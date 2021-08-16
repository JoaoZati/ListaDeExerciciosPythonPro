#%% 10 - Turno de trabalho

turno = input('Digite o seu turno: V = Vespertino, M = Matutino, N = Noturno: ').upper()

if turno == 'V':
    print('Boa Tarde')
elif turno == 'M':
    print('Bom Dia')
elif turno == 'N':
    print('Boa Noite')
else:
    print('Invalido')
