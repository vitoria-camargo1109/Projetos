"""
Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
As duas primeiras listas o usuário deverá digitar os valores, quando ele quiser terminar de
preencher a lista deverá digitar 0 (zero).
"""

lista1 = []
lista2 = []
lista3 = []

while True:
    n1 = int(input("Digite um número(0 para finalizar):"))
    if n1 == 0:
        break
    lista1.append(n1)

print('\n', lista1)

while True:
    n2 = int(input("Digite um número(0 para finalizar):"))
    if n2 == 0:
        break
    lista2.append(n2)

print('\n', lista2)

for num in lista1 + lista2:
    if num not in lista3:
        lista3.append(num)

print('\n', lista3)





