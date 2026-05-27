"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
ano_atual = int(input("Digite o ano atual: "))
maior = 0
menor = 0

for nascimento in range(1, 8):
    ano_nascimento = int(input("Digite o ano do seu nascimento: "))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f"{maior} são maiores de idade!")
print(f"{menor} são menores de idade!")