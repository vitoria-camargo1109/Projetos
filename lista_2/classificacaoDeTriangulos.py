"""Leia os três lados de um triângulo e informe se ele é
Equilátero (3 lados iguais), Isósceles (2 lados iguais)
ou Escaleno (todos diferentes)."""

l1 = float(input("Digite o valor do primeiro lado do triângulo: "))
l2 = float(input("Digite o valor do segundo lado do triângulo: "))
l3 = float(input("Digite o valor do terceiro lado do triângulo: "))

if l1 == l2 and l2 == l3:
    print("É um triângulo Equilátero!")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("É um triângulo Isósceles!")
else:
    print("É um triângulo Escaleno!")