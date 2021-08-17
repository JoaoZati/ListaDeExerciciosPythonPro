#%% 04 - Nome vertical em escala

"""
Nome na vertical em escada. Modifique o programa anterior de forma a 
mostrar o nome em formato de escada.
"""

string = input('Digite uma palavra: ')

for i in range(len(string)+1): print(string[:i])
