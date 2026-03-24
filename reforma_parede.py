def main():
    try:
        largura = float(input("Digite a largura da parede: "))
        altura = float(input("Digite a altura da parede: "))
    except ValueError:
        print("Valor inválido! Tente novamente")
        print("-------------------------------")
        main()
    else:
        area = largura * altura
        latas_necessarias = area // 15
        custo_lata = latas_necessarias * 120
        
        dias_trabalho = area / 10
        pintor = dias_trabalho * 15 + dias_trabalho* 150
        
        print(f"A área total a ser pintada é de {area:.2f}m²; a quantidade de latas necessárias são de {latas_necessarias}, custando {custo_lata:.2f} cada")
        print(f"O custo pelo trabalho do pintor foi de {pintor:.2f}, durante {dias_trabalho} dias de trabalho para finalizar a obra.")
        
main()       
        
        