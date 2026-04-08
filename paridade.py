def main():
    try:
        n = float(input("Digite um número: "))
    except ValueError:
        print("Número inválido! Por favor tente novamente.")
        print("-------------------------------------------")
        main()
    else:
        if n % 2 == 0:
            print("O número é par!")
        else:
            print("O número é impar")
        print("----------------")

main()