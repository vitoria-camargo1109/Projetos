"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

def opcao(v1, v2, sinal):
      if sinal == 1:
            print("-" * 30)
            print()
            soma = v1 + v2
            return print(f"{v1} + {v2} = {soma}")
            print()
            print("-" * 30)

      elif sinal == 2:
            print("-" * 30)
            print()
            multiplicacao = v1 * v2
            return print(f"{v1} X {v2} = {multiplicacao}")
            print()
            print("-" * 30)

      elif sinal == 3:
            if v1 > v2:
                  print("-" * 30)
                  print()
                  return print(f"O número {v1} é maior que o número {v2}")
                  print()
                  print("-" * 30)

            elif v2 > v1:
                  print("-" * 30)
                  print()
                  return print(f"O número {v2} é maior que o número {v1}")
                  print()
                  print("-" * 30)

            else:
                  print("-" * 30)
                  print()
                  print("Os dois números são iguais!")
                  print()
                  print("-" * 30)

print()
valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))

while True:
      print()
      print("-" * 30)
      print("Escolha uma opção:\n"
            "1 - somar\n"
            "2 - multiplicar\n"
            "3 - maior\n"
            "4 - novos números\n"
            "5 - sair do programa")
      print("-" * 30)
      print()

      while True:
            escolha = int(input("Escolha uma opção(de 1 á 5 apenas): "))
            print()

            if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
                  print("-" * 30)
                  print()
                  print("opção inválida, escolha outra de 1 á 5!")
                  print()
                  print("-" * 30)

            else:
                  break

      opcao(valor_1, valor_2, escolha)

      if escolha == 4:
            print("-" * 30)
            print()
            print("Escolha novos número: ")
            print()
            print("-" * 30)
            valor_1 = float(input("Digite o primeiro valor: "))
            valor_2 = float(input("Digite o segundo valor: "))
            print("-" * 30)
            print()



      elif escolha == 5:
            print()
            print("-" * 30)
            print()
            print("Volte sempre!")
            print()
            print("-" * 30)
            break


