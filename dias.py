def main():
    try:
        periodo = int(input("Digite o número de dias do período: "))
    except ValueError:
        print("Quantidade de dias inválido! Por favor tente novamente.")
        print("-------------------------------------------------------")
        main()
    else:
        semanas = periodo/7
        dias_restantes = periodo % 7
        print(f"O período foi de {int(semanas)} senana(s) e {dias_restantes} dia(s). ")
        
main()