#%% 18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data_imp = input('Digite uma data seguindo o formato dd/mm/aaaa: ')

def calcularbixesto(ano):
    if ano % 400 == 0:
        return True
    elif ano%4 == 0 and ano%100 != 0:
        return True
    
    return False
    
def verificarano(ano):
    if ano < 0 or ano > 9999:
        return True
    
    return False
    
def verificarmes(mes):
    if mes < 1 or mes > 12:
        return True
    
    return False

def verificarodia(dia, mes, ano):   
    if dia < 1 or dia > 31:
        return True
    
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia < 1 or dia > 30:
            return True
    elif mes == 2:
        if dia < 1 or dia > 29:
            return True
        elif not calcularbixesto(ano):
            if dia == 29:
                return True
            
    return False

def verificardata(data):
    
    try:
        dia = int(data[:2])
        mes = int(data[3:5])   
        ano = int(data[6:])
    except:
        print('Não foi possivel fazer os numeros inteiros: Verifique se forneceu nesse formato dd/mm/aaaa')
        return
        
    if verificarano(ano) == True:
        print('O ano da data não é valida')
        return
    
    if verificarmes(mes):
        print('O mes da data não é valida')
        return
    
    if verificarodia(dia, mes, ano):
        print('O dia da data não é valida')
        return
    
    print('A data é valida')
    
verificardata(data_imp)
