#%% 14 - 5 Perguntas

"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa 
sobre um crime. As perguntas são:
    
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma 
classificação sobre a participação da pessoa no crime. Se a pessoa 
responder positivamente a 2 questões ela deve ser classificada como 
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso 
contrário, ele será classificado como "Inocente".
"""

list_perguntas = ["Telefonou para a vítima?",
                "Esteve no local do crime?",
                "Mora perto da vítima?",
                "Devia para a vítima?",
                "Já trabalhou com a vítima?" ]

def input_sim_ou_nao(menssagem):
    while True:
        s = input(menssagem).upper()
        if s not in ['S', 'N']:
            print("Responda 'S' ou 'N'")
            continue
        return s

count = 0
for pergunta in list_perguntas:
    resposta = input_sim_ou_nao(pergunta +': ')
    if resposta == 'S': count += 1
    
if count == 2: print('"Suspeita"')
elif count == 3 or count == 4: print('"Cumplice"')
elif count == 5: print('"Assassino"')
else: print('"Inocente"')
