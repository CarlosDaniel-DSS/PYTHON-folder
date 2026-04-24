'''def main():
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
            if destino == 1 and idade >= 16 or destino == 2 and idade >= 16 or destino == 3 and idade >=18:
                
                #Custo do destino 
                if destino == 1:
                    custo_final = 10000.00
                elif destino == 2:
                    custo_final = 12000.00
                elif destino == 3:
                    custo_final = 15000.00
                    
                #Comparando com orçamento
                if orcamento < custo_final:
                    print(f"Viagem negada: Orçamento de R${orcamento:.2f} é insuficiente para o custo_final fixo de [{destino}](R${custo_final})")
                    
                #Validação do período e proficiẽncia
                elif fluencia_idioma >= 8:
                    duracao = 90
                    saldo_restante = orcamento - custo_final
                    if  saldo_restante / desejado < 500.00:
                        print("Viagem negada: Saldo restante insuficiente para manter")
                    else: 
                        print(f"Viagem aprovada! Destino: {destino}. Duração: {duracao} dias. Saldo para gastos diarios: R${saldo_restante}.")              
                
                elif fluencia_idioma >= 5 and fluencia_idioma <= 7:
                    duracao = 30
                    saldo_restante = orcamento - custo_final
                    if  saldo_restante / desejado < 500.00:
                        print("Viagem negada: Saldo restante insuficiente para manter")
                    else: 
                        print(f"Viagem aprovada! Destino: {destino}. Duração: {duracao} dias. Saldo para gastos diarios: R${saldo_restante}.")              
                
                elif fluencia_idioma < 5:
                    duracao = 15
                    saldo_restante = orcamento - custo_final
                    if  saldo_restante / desejado < 500.00:
                        print("Viagem negada: Saldo restante insuficiente para manter")
                    else: 
                        print(f"Viagem aprovada! Destino: {destino}. Duração: {duracao} dias. Saldo para gastos diarios: R${saldo_restante}.")              
                
                elif desejado > duracao:
                    print(f"Viagem negada: Sua fluência({fluencia_idioma}) permite apenas {duracao} dias, mas você solicitou {desejado} dias.")
                
        else:
            print("viagem negada: [Passaporte inválido] ou [Idade mínima para o destino não atingida]")

main()'''

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
        
        #variável que vai acumular ou não, invalidações das etapas doi código:
        erros = ""
        
        if passaporte == "não":
            erros = (f"\n[Passaporte inválido]")
        
        if not(destino == 1 and idade >= 16 or destino == 2 and idade >= 16 or destino == 3 and idade >=18):
            erros = (f"\n[Idade mínima para o destino não atingida]")
                
        #Custo do destino 
        if destino == 1:
            custo_final = 10000.00
        elif destino == 2:
            custo_final = 12000.00
        elif destino == 3:
            custo_final = 15000.00
                    
        #Comparando custo com orçamento
        if orcamento < custo_final:
            erros = (f"\nViagem negada: Orçamento de R${orcamento:.2f} é insuficiente para o custo_final fixo de [{destino}](R${custo_final})")
                    
        #Validação do período e proficiẽncia
        if fluencia_idioma >= 8:
            duracao = 90
        elif fluencia_idioma >= 5 and fluencia_idioma <= 7:
            duracao = 30      
        elif fluencia_idioma < 5:
            duracao = 15
        elif desejado > duracao:
            erros = (f"\nViagem negada: Sua fluência({fluencia_idioma}) permite apenas {duracao} dias, mas você solicitou {desejado} dias.")
           
        #Verificando orçamento para gastos diários(mínimo: R$500)      
        saldo_restante = orcamento - custo_final
        if saldo_restante / desejado < 500.00:
            erros = (f"\nSaldo restante insuficiente para manter o custo de R$500/dia pela duração de {desejado} dias ")
        
        #Resultado final:
        if erros == "":
            print(f"Viagem aprovada! \nDestino: {destino}. Duração: {duracao} dias. Saldo para gastos diarios: R${saldo_restante}.")              
        else:
            print("Viagem negada.")
            print(erros)
main()
