def main():
    try:
        sal_bruto_anual = float(input("Informe o salário bruto anual: "))
        rend_insentos_anual = float(input("Informe o total de gastos insentos durante o ano:  "))
        irrf_anual =  float(input("Informe a quantia de imposto ja descontada do salário durante o ano: "))
        
        print("------------------------------------------------------------------------------------------")
    except ValueError:
        print("Valor inválido! Tente novamente")
        print("-------------------------------")
        return main()
    else:
        #Fluxo de cálculos e regras(Tabela progressiva anual)
        
        #Etapa 1: Correção dos gastos anuais
        sal_bruto_anual = sal_bruto_anual - rend_insentos_anual
        
        #Etapa 2: Aplicação da Tabela Progressiva(Seleção Múltipla)
        if sal_bruto_anual <= 33912.00:
            imposto_devido = 0.00
        elif sal_bruto_anual <= 45012.00:
            imposto_devido = 0.075 * sal_bruto_anual - 2543.40
        elif sal_bruto_anual <= 67008.00:
            imposto_devido = 0.15 * sal_bruto_anual - 5919.30
        elif sal_bruto_anual <= 88848.00:
            imposto_devido = 0.225 * sal_bruto_anual - 10944.90
        else:
            imposto_devido = 0.275 * sal_bruto_anual - 15387.30
            
        #Etapa 3: Ajuste Final (Restituição ou imposto a pagar)
        restituicao = imposto_devido - irrf_anual
        
        #Resultado final
        print(f"Rendimento Total Anual: R${rend_insentos_anual:.2f}")
        print(f"Imposto que deveria ter sido pago: R${imposto_devido:.2f}")
        print(f"Imposto que foi pago antecipadamente: R${irrf_anual:.2f}")
        
        if restituicao < 0:
            print(f"\nVocê tem R${(restituicao * -1):.2f} a restituir")
        elif restituicao > 0:
            print(f"Você tem R${restituicao:.2f} a pagar")
        else:
            print("Saldo inexistente.")

main()

'''def main():
    try:
        sal_bruto_anual = float(input("Informe o salário bruto anual: "))
        rend_insentos_anual = float(input("Informe o total de gastos insentos durante o ano:  "))
        irrf_anual =  float(input("Informe a quantia de imposto ja descontada do salário durante o ano: "))
        
        print("------------------------------------------------------------------------------------------")
    except ValueError:
        print("Valor inválido! Tente novamente")
        print("-------------------------------")
        return main()
    else:
        #Fluxo de cálculos e regras(Tabela progressiva anual)
        
        #Etapa 1: Correção dos gastos anuais
        sal_bruto_anual = sal_bruto_anual - rend_insentos_anual
        
        #Etapa 2: Aplicação da Tabela Progressiva(Seleção Múltipla)
        if sal_bruto_anual <= 33912.00:
            imposto_devido = 0.00
        if sal_bruto_anual <= 45012.00:
            imposto_devido = 0.075 * sal_bruto_anual - 2543.40
        if sal_bruto_anual <= 67008.00:
            imposto_devido = 0.15 * sal_bruto_anual - 5919.30
        if sal_bruto_anual <= 88848.00:
            imposto_devido = 0.225 * sal_bruto_anual - 10944.90
        if sal_bruto_anual > 88848.00:
            imposto_devido = 0.275 * sal_bruto_anual - 15387.30
            
        #Etapa 3: Ajuste Final (Restituição ou imposto a pagar)
        restituicao = imposto_devido - irrf_anual
        
        #Resultado final
        print(f"Rendimento Total Anual: R${rend_insentos_anual:.2f}")
        print(f"Imposto que deveria ter sido pago: R${imposto_devido:.2f}")
        print(f"Imposto que foi pago antecipadamente: R${irrf_anual:.2f}")
        
        if restituicao < 0:
            print(f"\nVocê tem R${(restituicao * -1):.2f} a restituir")
        elif restituicao > 0:
            print(f"Você tem R${restituicao:.2f} a pagar")
        else:
            print("Saldo inexistente.")

main()'''
            
        
        
        