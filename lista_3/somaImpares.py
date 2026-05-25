"""
Faça um programa que calcule a soma entre todos os números que são múltiplos
de três e que se encontram no intervalo de 1 até 500.(apenas impares serão somados)
"""

soma = 0

for imp in range(1, 500):
    if imp % 2 == 1:
        soma = soma + imp

print(soma)