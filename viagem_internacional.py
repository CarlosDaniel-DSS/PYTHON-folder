def main():
    try:
        print("[Solicitação de dados]")
        
        desejado = int(input("Quantos dias durará a viagem?: "))
        destino = int(input("Qual o destino da viagem? [opções: '1' = Nova York, '2' = Paris, '3' = Toquio]: "))
        passaporte = input("Seu passaporte é válido? (Sim/Não): ").lower()
        orcamento = int(input("Informe seu orçamento disponível(R$): "))
        idade = int(input("Qual a sua idade?"))
        fluencia_idioma = float(input("Qual seu nível de fluência sobre o idioma local do destino? (avalie de 0 a 10): "))
        
        print("----------------------------------------------------------------------------------------------------------")
        
    except ValueError:
        print("Valor inválido! Tente novamente")
        print("-----------------------------------------------------------------------------------------------------")
        return main()
    else:
        #Fluxo de decisão e regra de auditoria
        
        #Filtro de documentação e identidade;
        if passaporte == "sim":
            if destino == 1 and idade >= 18 or destino == 2 and idade >= 16 or destino == 3 and idade >=16:
                
                #Custo do destino 
                if destino == 1:
                    custo = 10000.00
                elif destino == 2:
                    custo = 12000.00
                elif destino == 3:
                    custo = 15000.00
                    
                #Comparando com orçamento
                if orcamento < custo:
                    print(f"Viagem negada: Orçamento de R${orcamento:.2f} é insuficiente para o custo fixo de [{destino}](R${custo})")
                    
                #Validação do período e proficiẽncia
                elif fluencia_idioma >= 8:
                    duracao = 90
                    custo()
                elif fluencia_idioma >= 5 and fluencia_idioma <= 7:
                    duracao = 30
                    custo()
                elif fluencia_idioma < 5:
                    duracao = 15
                    custo()
                elif desejado > duracao:
                    print(f"Viagem negada: Sua fluência({fluencia_idioma}) permite apenas {duracao} dias, mas você solicitou {desejado} dias.")
                
                #Custo diário
                def custo():
                    saldo_restante = orcamento - custo
                    if saldo_restante / desejado < 500.00:
                        print("Viagem negada: Saldo restante insuficiente para manter")
                    else: 
                        print(f"Viagem aprovada! Destino: {destino}. Duração: {duracao} dias. Saldo para gastos diarios: R${saldo_restante}.")              
                
        else:
            print("viagem negada: [Passaporte inválido] ou [Idade mínima para o destino não atingida]")

main()
                
                
                
        