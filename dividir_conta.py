def main():
    try:
        amiguinhos = int(input("Digite o número de amiguinhos que irão pagar a continha: "))
        consumo = float(input("Digite o valor total gasto da mesa: "))
        taxa_lule = float(input("Digite o valor da taxinha do amor na conta: "))
    except ValueError:
        print("Valor inválido! Por favor tente novamente.")
        print("------------------------------------------")
        main()
    else:
        adicional = (taxa_lule/100) * consumo
        pagamento = consumo + adicional
        conta_individual = pagamento/3
        
        print(f"Cada amiguinho deve pagar {conta_individual:.2f} e ser feliz :D")

main()
        