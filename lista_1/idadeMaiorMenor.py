"""Exercício 2.11 (Operadores Lógicos): Faça um algoritmo que leia o ano de
nascimento de uma pessoa e o ano atual. Calcule a idade da pessoa e
armazene em uma variável do tipo lógica (booleana) se ela é maior de idade
(idade maior ou igual a 18 anos). Mostre a idade e o resultado lógico na tela."""

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento
maior_idade = False

if idade >= 18:
    maior_idade = True
    print(idade,maior_idade)
else:
    print(idade,maior_idade)
