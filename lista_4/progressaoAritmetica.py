# An = A1 + (n - 1) . r
# R = A2 - A1

"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
dez_termos = 10

an = primeiro_termo + (dez_termos - 1) * razao

for pa in range(primeiro_termo, an + razao, razao):
    print(pa)