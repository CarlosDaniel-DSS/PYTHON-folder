def main():
    try:
        compra = float(input("Digiter o valor total da compra: "))
    except ValueError:
        print("Valor inválido! Por favor tente novamente.")
        print("------------------------------------------")
        main()
    else:
        if compra > 200:
            print(f"A sua compra recebe um desconto de 10%, ficando R${(compra - compra * 0.1)}")
        else:
            print(f"O valor final da compra ée de R${compra:.1f}")
            
main()