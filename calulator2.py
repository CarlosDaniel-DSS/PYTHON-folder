def main():
    x = float(input("digite o valor x:")) #pega o valor digitado

    result_quadrado = formatar(calcular_quadrado(x)) 
    result_cubo = formatar(calcular_cubo(x))

    print(f"o quadrado de {formatar(x)} e o cubo de {formatar(x)} são, repectivamente, {result_quadrado} e {result_cubo}") #exibe o resultado

def calcular_quadrado(x):
    return x ** 2 

def calcular_cubo(x):
    return x ** 3

def formatar(x):
    x = f"{x:_.2f}" #define o limite de casas decimais para duas
    return x.replace(".", ",").replace("_", ".") #muda os separadores do número para o modelo br 
        
main()
