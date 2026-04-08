def main():
    try:
        n1 = float(input("Digite um número: "))
        n2 = float(input("digite um número diferente do anterior: "))
        if n1 != n2:
            pass
        else:
            print("Tente com números diferentes!")
            print("-----------------------------")
            return main()
    except ValueError:
        print("Número inválido! Por favor tente novamente.")
        print("-------------------------------------------")
        main()
    else:
        if n1 > n2:
            print(f"{n1} é maior que {n2}.")
        else:
            print(f"{n2} é maior que {n1}.")
        print("-----------------------")
        
main()