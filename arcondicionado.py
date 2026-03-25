def main():
    try:
        largura = float(input("Digite a largura da parede: "))
        altura = float(input("Digite a altura da parede: "))
    except ValueError:
        print("Valor inválido! Tente novamente")
        print("-------------------------------")
        main()
    else:
        potencia_necessaria = largura * altura * 600
        consumo_aparelho = potencia_necessaria / 12000 * (1.2 * 8)
        preco = consumo_aparelho * 0.85
        
        print(f"O aparelho gastaria {consumo_aparelho}kWh, custando R${preco:.1f}.")

main()