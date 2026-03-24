def main():
    try:
        conta = float(input("Digite a conta final(R$): "))
        pagamento = float(input("Informe o pagamento da conta(R$): "))
        notas = [50, 10, 5]
    except ValueError: 
        print("Valor inválido! Tente novamente.")
        print("--------------------------------")
        main()
    else:
        if pagamento >= conta:
            troco = (pagamento % conta) // 5
            
               
                
            
            print(troco)
        else: 
            print("Pagamento insuficiente.")

main()
            
        