"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
foi o maior e o menor peso lidos.
"""

peso = 0
maior = 0
menor = 0

for pessoa in range(1, 6):
    kg = float(input("Digite o seu peso: "))

    if pessoa == 1:
        maior = kg
        menor = kg

    if maior < kg:
        maior = kg

    if menor > kg:
        menor = kg

print(f"Maior peso: {maior}")
print(f"Menor peso: {menor}")
