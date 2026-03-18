def main ():
    try:
        potencia  = float(input("Digite a potẽncia(em Watts) do eletrodoméstico: "))
        tempo = float(input("Digite o tempo que o eletrodoméstico ficou ligado: "))
        valor_kwh = float(input("Digite o preço do Kw/h na sua região: "))
    except ValueError:
        print("Valor inválido! Tente novamente")
        print("-------------------------------")
        main()
    else:
        custo = (potencia*tempo)/1000 * valor_kwh
        
        print(f"O custo total de energia gasta pelo eletrodoméstico foi de {custo:.2f}")

main()