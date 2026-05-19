"""Faça um programa que solicite ao usuário um número inteiro (n).
Este número deverá ser pesquisado na lista abaixo.
Ao final apresentar as mensagens: “n encontrado na posição x.” ou “n não encontrado.”
lista_de_numeros = [12, 15, 7, 9, 27, 34]"""

lista = [12, 15, 7, 9, 27, 34]
numero = int(input("Digite um número:"))
encontrado = False

for i, k in enumerate(lista):
    if numero == lista[i]:
        print(f"{numero} encontrado na posição {i}")
        encontrado = True
        break
if not encontrado:
    print(f"{numero} não encontrado")