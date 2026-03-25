def main():
    try:
        hidrometro_anterior = float(input("Digite a leitura passada(m3) do hidrômetro: "))
        hidrometro_atual = float(input("Digite a leitura atual(m3) do hidrômetro:"))
    except ValueError:
        print("Valor inválido! Tente novamente.")
        print("--------------------------------")
        main()
    else: 
        consumo = hidrometro_atual - hidrometro_anterior
        valor_agua = consumo * 4.5
        esgoto = consumo * 0.8
        custo_total = valor_agua + esgoto + 12
        
        print(f"O consumo total de água foi de {consumo:.1f}L/m³, o custo da água foi de R${valor_agua:.1f};")
        print(f"O valor do esgoto foi de R${esgoto:.1f} e o custo total: R${custo_total:.1f}.")
        print("---------------------------------------------------------------------------------------------")
        
main()