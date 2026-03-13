def main():
    try:
        vendedor = input("Digite o nome do vendedor: ")
        if vendedor.isdigit() or vendedor == "":
            print("Nome inválido! Por favor ensira outro.")
            main()
        else:
            vendas = int(input("Digite o número de carros vendidos por esse vendedor: "))
            valor_vendas = float(input("Digite o valor total das vendas dos carros: "))
    except ValueError:
        print("Quantidade inválida! Por favor, tente novamente.")
        print("------------------------------------------------")
        main()
    else:
        comissao = 150 * vendas
        adicional = (5/100) * valor_vendas
        salario = 2000 + comissao + adicional
        
        print(f"O vendedor {vendedor} vendeu {vendas} carros e seu salário é de {salario:.2f}")
        print("------------------------------------------------------------------------------")
    
main()