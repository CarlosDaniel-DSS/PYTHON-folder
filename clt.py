#hora trabalhada, ganho por hora = inss, sal_brut, sal_liquid, contrato sindical

def clt():
    try:
        ganho_hora = float(input("Digite o quanto você ganha por hora: "))
        horas_trabalhadas = float(input("Digite quantas horas você trabalhou no mês: "))
    except ValueError:
        print("Horas incorretas, digite um valor válido")
        clt()
    else:
        sal_bruto = ganho_hora * horas_trabalhadas
        inss = sal_bruto * 0.11
        contrato_sindical = sal_bruto * 0.55
        sal_liquid = sal_bruto - inss - contrato_sindical
        
        print(f"O valor do seu salário bruto é {sal_bruto}.")
        print(f"O valor do seu inss é {inss} e do seu contrato sindical é {contrato_sindical}.")
        print(f"Portanto, o valor do seu salário líquido é de {sal_liquid}.")

clt()
     
        
        