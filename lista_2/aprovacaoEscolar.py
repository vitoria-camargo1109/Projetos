"""Faça um programa que receba a média de um aluno e diga se ele está
"Aprovado" (média >=6), em "Exame" (média entre 4 e 5.9) ou
"Reprovado" (média abaixo de 4)"""

media = float(input("Digite a média: "))

if media >= 6:
    print("Você está Aprovado!")
elif media >= 4:
    print("Você está em Exame.")
elif media < 4:
    print("Você está Reprovado...")