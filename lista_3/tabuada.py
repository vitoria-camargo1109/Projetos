"""
Faça uma tabuada mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for.
"""

start = True

while start:
    print("TABUADA")
    print()
    numero = int(input("Digite um número para visualizar sua tabuada: "))
    print()
    print(f"TABUADA DO {numero}")
    print()
    for tab in range(0, 11):
        print(f"{numero} X {tab} = {numero * tab}")

    while True:
        escolha = input("Você deseja continuar?\n" 
                        "(S) para sim e (N) para não: ")

        if escolha.upper() == "S":
            break
        if escolha.upper() == "N":
            start = False
            break

print()
print("Volte Sempre! :)")





