def main():
    try:
        val_carro = float(input("Digite o preço do carro: "))
        juros_mensal = float(input("Digite o juros mensal(%): "))
        parcelas = int(input("Digite o total de parcelas do pagamento do carro: "))
    except ValueError:
        print("Valor inválido! Tente novamente")
        print("-------------------------------")
        main()
    else:
        juros_carro = val_carro * juros_mensal * parcelas
        val_parcelas = (val_carro + juros_carro) / parcelas
        custo_total = val_parcelas * parcelas
        val_juros = custo_total - val_carro
        
        print(f"O valor total do juros é de R${val_juros:.1f}, sendo o valor total do carro R${custo_total:.1f} a R${val_parcelas:.1f} cada.")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        
main()
        
        
        