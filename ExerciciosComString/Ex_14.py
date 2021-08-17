#%% 14 - Leet Speak Generator

"""
Leet spek generator. Leet é uma forma de se escrever o alfabeto latino 
usando outros símbolos em lugar das letras, como números por exemplo. 
A própria palavra leet admite muitas variações, como l33t ou 1337. O uso 
do leet reflete uma subcultura relacionada ao mundo dos jogos de 
computador e internet, sendo muito usada para confundir os iniciantes e 
afirmar-se como parte de um grupo. Pesquise sobre as principais formas 
de traduzir as letras. Depois, faça um programa que peça uma texto e 
transforme-o para a grafia leet speak.
"""

replacement_words = {'hacker': 'haxor',
                      'elite': 'eleet',
                       'a': '4',
                       'e': '3',
                       'l': '1',
                       'o': '0',
                       't': '+',
                       'k': '|<',
                       's': '5'}

my_string = input('Digite palavra para passar em leet spek: ') #'I am an skilled hacker elite yet'
new_string = my_string

for key, value in replacement_words.items():
    new_string = new_string.replace(key, value)

print(f'{new_string}')
