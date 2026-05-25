"""Exercício 2.1: Duas variáveis (A e B) possuem valores distintos
(A = 5 e B = 10, por exemplo). Crie um algoritmo que armazene
esses valores nas 2 variáveis e efetue a troca de valores de forma que a
variável A passe a possuir o valor de B e que a variável B passe
a possuir o valor de A. Ao final mostrar esses valores trocados."""

a = 5
b = 10

print(f"valor iniciais de A e B: {a} e {b}")

aux = a
a = b
b = aux


print(f"valor trocados de A e B: {a} e {b}")