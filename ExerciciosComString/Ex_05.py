#%% 05 - Nome em escala invertida

"""
Nome na vertical em escada invertida. Altere o programa anterior de modo 
que a escada seja invertida.
"""

string = input('Digite uma palavra: ')

for i in range(len(string)+1, -1, -1): print(string[:i])
