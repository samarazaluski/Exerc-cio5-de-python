codigo = int(input("Digite o código:"))

match codigo:
    case 1:
        print("Caneta - 1.20")
    case 2:

        print("Carderno - 4.50")

    case 3:
        print("lapis - 0.80")

    case 4:
        print("Borracha - 1.00")

    case 5:
        print("regua - 1.50")

    case _:
        print("Código invalido!")
