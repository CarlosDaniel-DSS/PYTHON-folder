renda_mensal = ''
imposto_retido = ''
isencao_mensal = ''
cnt = 0
acu_renda = 0
acu_retido = 0
acu_insencao = 0

while cnt < 12:
    renda_mensal = input("Digite o salário bruto do mês (em R$): ")
    insencao_mensal = input("Digite a quantia insentado mês (em R$): ")
    imposto_retido = input("Informe o imposto já retiddo no mês: ")
    
    print("----------------------------------------------------------")
    try:
        acu_renda += float(renda_mensal)
        acu_insencao += float(insencao_mensal)
        acu_retido += float(imposto_retido)
    except ValueError as err:
        print("Nota inválida")
        print(err)
        break
    else:
        cnt += 1
else:
    if cnt > 0:
        
        #definindo INSS por faixa salarial
        
        #Definindo o ajuste de imposto pra cada faixa salarial anual
        if acu_renda <= 29145.60:
            ajuste_imposto = 0.00
        elif acu_renda <= 33919.80:
            ajuste_imposto = acu_renda * 0.075 - (2185.92 + acu_retido)
        elif acu_renda <= 45012.60:
            ajuste_imposto = acu_renda * 0.15 - (4729.91 + acu_retido)
        elif acu_renda <= 55976.16:
            ajuste_imposto = acu_renda * 0.225 - (8105.85 + acu_retido)
        else:
            ajuste_imposto = acu_renda * 0.275 - (10904.66 + acu_retido)
            
        imposto_final = ajuste_imposto - acu_insencao
        
        diferenca = imposto_final - acu_insencao
        if diferenca > 0:
            print(f"A renda anual é de R${acu_renda:.2f}, com insentos de R${acu_insencao:.2f}. Logo você tem R${imposto_final:.2f} a pagar!")
        elif diferenca < 0:
            print(f"A renda anual é de R${acu_renda:.2f}, com insentos de R${acu_insencao:.2f}. Logo você tem R${imposto_final:.2f} a receber!")
        else:
            print(f"Saldo inexistente.")
        
'''renda_mensal = ''
isencao_mensal = ''
cnt = 0
acu_renda = 0
acu_isencao = 0

while cnt < 12:
    renda_mensal = input("Digite o salário bruto do mês (em R$): ")
    isencao_mensal = input("Digite a quantia isenta do mês (em R$): ")
    
    print("----------------------------------------------------------")
    
    try:
        acu_renda += float(renda_mensal)
        acu_isencao += float(isencao_mensal)

    except ValueError as err:
        print("Valor inválido")
        print(err)
        break

    else:
        cnt += 1

else:
    if cnt > 0:

        # Definindo o ajuste de imposto para cada faixa salarial anual
        if acu_renda <= 29145.60:
            ajuste_imposto = 0.00

        elif acu_renda <= 33919.80:
            ajuste_imposto = acu_renda * 0.075 - 2185.92

        elif acu_renda <= 45012.60:
            ajuste_imposto = acu_renda * 0.15 - 4729.91

        elif acu_renda <= 55976.16:
            ajuste_imposto = acu_renda * 0.225 - 8105.85

        else:
            ajuste_imposto = acu_renda * 0.275 - 10904.66

        imposto_final = ajuste_imposto - acu_isencao

        print(f"Renda anual: R${acu_renda:.2f}")
        print(f"Total de isenções: R${acu_isencao:.2f}")
        print(f"Imposto anual devido: R${imposto_final:.2f}")'''
        