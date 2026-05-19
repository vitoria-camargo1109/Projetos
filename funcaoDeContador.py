"""Faça um programa que tenha uma função chamada contador(), que receba
três parâmetros: início, fim e passo. Seu programa tem que realizar três
contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

def contador(x, y, z):
    if x > y:
        z = -z

    for cont in range(x, y, z):
        print(cont, end = ' ')
    print()

contador(1, 10, 1)

contador(10, 0, 2)

i = int(input('Digite o primeiro número:'))
f = int(input('Digite o último número:'))
p = int(input('Digite o passo:'))

contador(i, f, p)