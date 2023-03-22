x = float(input("Digite o valor de x:"))

opcao= int(input("Digite a opção(1-3):"))

match opcao:

    case 1:
        x = x + 5

    case 2:
        x = x - 4

    case 3:
        x= 2 * x

    case _:
        print("Opção invalida")

print(f"Novo valor de x: {x:.2f}")