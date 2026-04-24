def main():
    try:
        print("[SOLICITAÇÃO DE DADOS]")
        
        print(f"\nOpções: 1- Sport, 2- SUV Luxury, 3- Eletric")
        categoria_carro = int(input("Escolha a categoria de carros a ser alugado(digitando seu respectivo número): "))
        renda_mensal = float(input("Informe sua renda mensal(R$): "))
        idade = int(input("Qual a sua idade?(anos): "))
        tempo_cnh = int(input("Informe há quantos anos possui CNH: "))
        pontuacao_cnh = int(input("Quantos pontos possui na carteira?: "))
        valor_carro = float(input("Qual o valor do carro desejado?: "))
        
    except ValueError:
        print("Valor(es) inválido(s)! Tente novamente.")
        print("---------------------------------------")
        return main
    else: 
        #Definindo variável que armazenará possíveis erros de validações
        erros = ""
        #Filtro de Experiência e Segurança(Idade e CNH)
        
        if categoria_carro == 2 or categoria_carro == 3 and idade >= 21 and tempo_cnh >= 2:
            pass
        elif categoria_carro == 1 and idade >= 25 and tempo_cnh >= 5:
            pass
        else:
            erros = "Assinatura negada: Experiência insuficiente para a categoria selecionada."
            
        #Análise de riscos(pontos na carteira)
        if erros == "" and categoria_carro == 1 or categoria_carro == 2 and pontuacao_cnh <= 20:
            pass  
        elif categoria_carro == 3 and pontuacao_cnh <=10:
            pass
        else:
            erros = "\nAssinatura Negada: Pontuação na CNH excede limite de segurança."
            
        #Verificação de crédito(limite por renda)
        if erros == "" and renda_mensal <= 5000.00 and valor_carro <= 80000.00:
            pass
        elif renda_mensal <= 10000.00 and valor_carro <= 150000.00:
            pass
        elif valor_carro <= 300000.00:
            pass
        else:
            erros = (f"\nAssinatura negada: Valor do veículo(RS=${valor_carro:.2f} imcompatível com a renda mensal.)")
        
        #Cálculo da mensalidade e comprometimento
        mensalidade_assinatura = 0.015 * valor_carro
        if erros == "" and mensalidade_assinatura >  0.3 * renda_mensal:
            erros = (f"\nAssinatura negada: Mensalidade de R${mensalidade_assinatura} excede o limite de 30% da renda.")
        else:
            pass
        
        #Resultado final
        if erros == "":
            print(f"CONTRATO LIBERADO! Categoria: {categoria_carro}, Carro: R${valor_carro},")
            print(f"Mensalidade de: R${mensalidade_assinatura:.2f}. Aproveite seu veículo!")
        else:
            print(f"PROPOSTA RECUSADA. Motivos:")
            print(erros)
        
main()   
