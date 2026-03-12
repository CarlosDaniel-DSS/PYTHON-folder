def main():
    
    #Mostra as opções de conversões pro usuário escolher
    opcoes = [
    "1 - USD para EUR e EUR para USD",
    "2 - USD para BRL e BRl para EUR",
    "3 - BRL para EUR e EUR para BRL",
    ]
    
    for opcao in opcoes:
        print(opcao)
    
    #Chamando a função escolhida pelo usuário
    try:
        escolher = int(input("Escolha o número da respectiva opção de conversão desejada: "))
    except ValueError:
        print("por favor, escolha um dos números das opções")
        main()
    else:
        if escolher == 1:
            usd_e_eur()
        elif escolher == 2:
            usd_e_brl()
        elif escolher == 3:
            brl_e_eur()
        else:
            print("Escolha novamente.")
            main()


#Definido cada função de conversão de moedas
def usd_e_eur():
    try:
        cotação_usd_para_eur = float(input("Digite a cotação para converter usd para eur: "))
        montante_usd = float(input("Digite o montante de dólares: "))
        montante_eur = float(input("Digite o montante de euros: ")) 
    except ValueError:
        print("Valor inválido! Tente novamente.")
        usd_e_eur()
    else:
        eur_final = montante_usd * cotação_usd_para_eur
        usd_final = montante_eur / cotação_usd_para_eur
        
        print(f"O valor final da conversão de dolar para euro é de {eur_final}")
        print(f"Enquanto o inverso, de euro para dolar é de {usd_final}")
        
def usd_e_brl():
    try:
        cotação_usd_para_brl = float(input("Digite a cotação para converter usd para brl: "))
        montante_usd = float(input("Digite o montante de dólares: "))
        montante_brl = float(input("Digite o montante de reais: ")) 
    except ValueError:
        print("Valor inválido! Tente novamente.")
        usd_e_brl()
    else:
        brl_final = montante_usd * cotação_usd_para_brl
        usd_final = montante_brl / cotação_usd_para_brl
        
        print(f"O valor final da conversão de dolar para reais é de {brl_final}")
        print(f"Enquanto o inverso, de drais para dolar é de {usd_final}")
    
def brl_e_eur():
    try:
        cotação_brl_para_eur = float(input("Digite a cotação para converter usd para brl: "))
        montante_brl = float(input("Digite o montante de reais "))
        montante_eur = float(input("Digite o montante de euros: ")) 
    except ValueError:
        print("Valor inválido! Tente novamente.")
        brl_e_eur()
    else:
        eur_final = montante_brl * cotação_brl_para_eur
        brl_final = montante_eur / cotação_brl_para_eur
        
        print(f"O valor final da conversão de reais para euros é de {eur_final}")
        print(f"Enquanto o inverso, de euros para reais é de {brl_final}")

main()
        
