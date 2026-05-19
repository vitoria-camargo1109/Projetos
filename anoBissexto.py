"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

a = int(input('Digite um ano:'))

if a % 4 == 0 and a % 100 == 0 and a % 400 == 0:
    print(f'O ano {a} é um ano bissexto!')
else:
    print(f'O ano {a} não é um ano bissexto!')
