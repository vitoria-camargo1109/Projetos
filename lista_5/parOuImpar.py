"""
Crie uma função chamada eh_par que receba um número inteiro como parâmetro.
A função deve retornar True se o número for par e False se for ímpar.
"""

def eh_par(numero):
    if numero % 2 == 0:
        return True
    elif numero % 2 == 1:
        return False

numero = int(input("Digite um número: "))

print(eh_par(numero))