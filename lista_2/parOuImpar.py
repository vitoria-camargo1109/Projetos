"""
Receba um número inteiro e determine se ele é par ou ímpar
utilizando o operador de resto da divisão (%).
"""

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"O {num} é um número par!")
else:
    print(f"O {num} é um número ímpar!")