"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

2, 3, 5 e 11
"""

numero = int(input("Digite um número: "))
total_de_divisoes = 0

for num in range(1, numero + 1):
    if numero % num == 0:
        total_de_divisoes += 1

if total_de_divisoes == 2:
    print("É um número primo!")
else:
    print("Não é um número primo!")