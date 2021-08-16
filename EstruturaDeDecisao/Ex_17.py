#%% 17 - ano bissexto

ano_imp = int(input('Insira o ano aqui: '))

def calcularbixesto(ano):
    if ano % 400 == 0:
        print('O ano é bixesto')
        return
    elif ano%4 == 0 and ano%100 != 0:
        print('O ano é bixesto')
        return
    
    print('O ano não é bixesto')
    
calcularbixesto(ano_imp)
