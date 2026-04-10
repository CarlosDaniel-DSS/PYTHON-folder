def main():
    try:
        vel_carro = float(input("Digite a velocidade do carro(km/h): "))
        via = input("Digite a via em que o carro passou(urbana, rodovia ou escolar): ").lower()
        if via == "urbana" or via == "rodovia" or via == "escolar":
            pass
        else:
            print("Escolha uma das vias possíveis!")
            return main()
    except ValueError:
        print("Valor inválido! Por favor, tente novamente.")
        print("-------------------------------------------")
        main()
    else:
        #Infração em via urbana
        if via == "urbana" and vel_carro > 60:
            if vel_carro <= 72:
                print("Multa leve! devido ao excesso de velociade(até 20%).")
            elif vel_carro <= 90:
                print("Multa grave! devido ao grande excesso de velocidade")
            else:
                print("Multa gravíssima e suspensão da carteira por enorme infração da velocidade permitida.")
                
        #Infração em rodovia
        elif via == "rodovia" and vel_carro > 110:
            if vel_carro <= 132:
                print("Multa leve! devido ao excesso de velociade(até 20%).")
            elif vel_carro <= 165:
                print("Multa grave! devido ao grande excesso de velocidade")
            else:
                print("Multa gravíssima e suspensão da carteira por enorme infração da velocidade permitida.")
            
        #Infração em via escolar
        elif via == "escolar" and vel_carro > 30:
            if vel_carro <= 36:
                print("Multa leve! devido ao excesso de velociade(até 20%).")
            elif vel_carro <= 45:
                print("Multa grave! devido ao grande excesso de velocidade")
            else:
                print("Multa gravíssima e suspensão da carteira por enorme infração da velocidade permitida.")
        
        #Não houve infração
        else:
            print("Parabéns! Você é um bom motorista")
    
main()
                
            
            
            
                
         