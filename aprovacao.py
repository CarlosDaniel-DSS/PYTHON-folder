def main():
    try:
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
    except ValueError:
        print("Número inválido! Por favor tente novamente.")
        print("-------------------------------------------")
        main()
    else:
        if (n1 + n2)/2 >= 6:
            print("Aprovado.")
        else:
            print("Reprovado.")
        print("-------------------------------------------")

main()