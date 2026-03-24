def main():
    try:
        distancia = float(input("Digite a distância percorrida(KM): "))
        preco_diesel = float(input("Digite o preço do diesel na sua região: "))
        frete = float(input("Digite o valor do frete recebido: "))
    except ValueError:
        print("Valor inválido! Tente novamente")
        print("-------------------------------")
        main()
    else:
        litros_gastos = distancia / 3.5
        pedagio = (distancia // 100) * 9.5
        manutencao = 0.20 * distancia
        gasto = preco_diesel * litros_gastos
        
        lucro = frete - (gasto + pedagio + manutencao)
        
        print(f"O gasto com combustível foi de {gasto:.1f}, o gasto com pedágio foi de {pedagio:.1f}")
        print(f"O gasto com manutencao foi de {manutencao:.1f} e o lucro final líquido foi de {lucro:.1f}")
        
main()