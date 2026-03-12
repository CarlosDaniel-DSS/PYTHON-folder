def main():
    try:
        odometro_inicial = int(input("Digite kilometragem inicial do seu dia (antes de começar o trabalho): "))
        odometro_final = int(input("Digite a kilometragem final do seu dia (após o fim do dia de trabalho): "))
        rendimento = float(input("Digite o valor total ganho com pedágio hoje: "))
        combustivel = float(input("Digite o valor local do combustível (na sua região): "))
        litros_gastados = float(input("Digite o valor em litros consumidos no dia: "))
    except ValueError:
        print("Valor inválido! Por favor tente novamente, se atentando aos valores digitados.")
        print("------------------------------------------------------------------------------")
        main()
    else:
        media_km = odometro_final - odometro_inicial
        consumo = media_km / litros_gastados
        lucro = rendimento - (consumo * combustivel)
        
        print(f"A sua média de consumo no expediente de hoje foi de {consumo:.2f}Km/L e o seu lucro foi de {lucro:.2f}")
        print("-------------------------------------------------------------------------------------------------------")

main()