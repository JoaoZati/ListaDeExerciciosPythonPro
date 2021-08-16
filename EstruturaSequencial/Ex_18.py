#%% 18 - Tamanho do arquivo MB

"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps), calcule e informe o 
tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_arquivo = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a velocidade de download em Mbps: '))

tempo_segundos = tamanho_arquivo/velocidade

def rounddown_min(num):
    segundos = num%60
    minutos = (num - segundos)/60
    
    return minutos, segundos

Qt_minutos, Qt_segundos = rounddown_min(tempo_segundos)

print(f"""
Seu download demorará: 
{tempo_segundos} segundos
ou
{Qt_minutos} minutos e {Qt_segundos} segundos
      """)
