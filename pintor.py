def main():
    try:
        altura = float(input("Digite a altura(em metros) da parede: "))
        largura = float(input("Digite a largura(em metros) da parede: "))
    except ValueError: 
        print("Valor inválido! Por favor tente novamente.")
        print("------------------------------------------")
        main()
    else:
        parede = altura * largura
        litros_necessarios = parede/3
        latas_necesarias = litros_necessarios/5
        preco_pintura = latas_necesarias * 80
        
        print(f"A área da parede é {parede:.2f}m², serão necessários {litros_necessarios:.2f} litros de tinta.")
        print(f"Sabendo disso, serão necessárias {latas_necesarias:.1f} latas de 5L de tinta, custando {preco_pintura:.2f} no total.")
        
main()
        
    