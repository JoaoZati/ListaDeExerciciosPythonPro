#%% 07 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

aresta_quadrado =  float(input('Digite um valor da aresta: '))
area_quadrado = aresta_quadrado**2
area_quadrado_x2 = area_quadrado*2

print(f'O dobro da área do quadrado de aresta {aresta_quadrado} é igual a : {area_quadrado_x2}')
