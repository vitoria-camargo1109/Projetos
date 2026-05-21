"""Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos
digitados, em ordem crescente."""

lista = []

while True:
    valores = int(input("Digite um número(Digite 0 para finalizar): "))

    if valores == 0:
        break
    if valores not in lista:
        lista.append(valores)
    else:
        print("Esse número já existe na lista, escolha outro.")

    lista.sort()

print(lista)