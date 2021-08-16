#%% 16 - Fibonnaci até 500

a0 = 0
a1 = 0
fibo = 1
inicio = True
    
while True:
    if not inicio:
        fibo = a1 + a0
    inicio = False
    
    print(f'{fibo}')
    if fibo >= 500:
        break
    a0 = a1
    a1 = fibo
