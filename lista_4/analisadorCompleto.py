"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do
programa, mostre: a média de idade do grupo, qual é o nome do homem
mais velho e quantas mulheres têm menos de 20 anos.
"""

soma = 0
media = 0
mulher = 0
maior = 0
nome_velho = ""
menos_vinte = 0

for info in range(1, 5):

    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    genero = str(input("Digite seu gênero: "))



    print()
    print("-----PRÓXIMO-----")
    print()


    soma += idade
    media = soma / 4

    if genero.lower() == "masculino":
        if idade > maior or maior == 0:
            maior = idade
            nome_velho = nome

    if genero.lower() == "feminino":
        if idade < 20:
            menos_vinte += 1

print("O homem mais velho é: ")
print(f"----- {nome_velho} -----")
print()
print(f"{menos_vinte} mulheres são menores de 20 anos!")


