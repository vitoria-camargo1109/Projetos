"""Leia os três lados de um triângulo e informe se ele é
Equilátero (3 lados iguais), Isósceles (2 lados iguais)
ou Escaleno (todos diferentes)."""

start = True
start1 = True

while start:

    l1 = float(input("Digite o valor do primeiro lado do triângulo: "))
    l2 = float(input("Digite o valor do segundo lado do triângulo: "))
    l3 = float(input("Digite o valor do terceiro lado do triângulo: "))

    if l1 == l2 and l2 == l3:
        print("É um triângulo Equilátero!")
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print("É um triângulo Isósceles!")
    else:
        print("É um triângulo Escaleno!")

    while True:

        print()
        print("Deseja adicionar outros valores?")
        print()
        print("-" * 30)
        print()
        print("Deseja continuar?")
        print("1- Sim\n"
              "2- Não")
        escolha = int(input("Escolha: "))

        while True:
            if escolha != 1 and escolha != 2:
                print("Opção inválida, Tente novamente!")
                escolha = int(input("Sim ou não?: "))
                break
            else:
                break

        if escolha == 1:
            break
        elif escolha == 2:
            start = False
            break


print("Volte sempre!")