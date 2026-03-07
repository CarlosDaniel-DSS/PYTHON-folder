def main():
    
    '''Definindo que, para cada escolha de figura na função 'escolher', será chamado a sua respectiva função  
    responsável por calcular a área'''
    
    escolher = input(
        "Escolha uma figura para calcular sua área:\n"
        "(triangulo, quadrado, retangulo, trapezio, losango, circulo\n"
        "ou escolha 'sair' para deixar o programa): "
        ).lower().strip()
     
    if escolher == "sair":
        sair()
    elif escolher == "triangulo":
        area_triangulo()
    elif escolher == "quadrado":
        area_quadrado()
    elif escolher == "retangulo":
        area_retangulo()
    elif escolher == "trapezio":
        area_trapezio()
    elif escolher == "losango":
        area_losango()
    elif escolher == "circulo":
        area_circulo()   
    else:
        print("Escolha inválida, tente novamente.")
        main()

#Definindo a saída do programa
def sair():
    print("Programa encerrado")
        
#Definindo a função responsável por pedir a unidade de medida dos valores usados no cálculo da área
def pedir_unidade():
    unidades_validas = ["cm", "m", "km"]
    
    while True:
        unidade = input("Escolha a unidade de media (cm, m, km): ")
        
        if unidade in unidades_validas:
            return unidade
        else:
            print("Unidade inválida! Tente novamente.")

#Definindo as função responsáveis por pedir os dados de cada figura e realizar o cálculo de sua área.
def area_triangulo():
    try:
        unidade: None = pedir_unidade()
        base = float(input("Digite o valor da base: "))
        altura = float(input("Digite o valor da altura: "))
    except ValueError:
        print("Os valores digitados precisam ser numéricos!\nTente novamente:")
        area_triangulo()
    else:
        area = base * altura /2
        print(f"A área do triângulo é {area}{unidade}²")
    
def area_quadrado():
    try:
        unidade: None = pedir_unidade()
        base = float(input("Digite o valor da base: "))
    except ValueError:
        print("Os valores digitados precisam ser numéricos!\nTente novamente:")
        area_quadrado()
    else:
        area = base ** 2
        print(f"A área do quadrado é {area}{unidade}²")
    
def area_retangulo():
    try:
        unidade: None = pedir_unidade()
        base = float(input("Digite o valor da base: "))
        altura = float(input("Digite o valor da altura: "))
    except ValueError:
        print("Os valores digitados precisam ser numéricos!\nTente novamente:")
        area_retangulo()
    else:
        area = base * altura 
        print(f"A área do retângulo é {area}{unidade}²")
    
def area_trapezio():
    try:
        unidade: None = pedir_unidade()
        base_menor = float(input("Digite o valor da base menor: "))
        base_maior = float(input("Digite o valor da base maior: "))
        altura = float(input("Digite o valor da altura"))
    except ValueError:
        print("Os valores digitados precisam ser numéricos!\nTente novamente:")
        area_trapezio()
    else:      
        area = (base_menor + base_maior) * altura / 2
        print(f"A área do trapézio é {area}{unidade}²")
    
def area_losango():
    try:
        unidade: None = pedir_unidade()
        diagonal_menor = float(input("Digite o valor da diagonal menor: "))
        diagonal_maior = float(input("Digite o valor da diagonal maior: "))
    except ValueError:
        print("Os valores digitados precisam ser numéricos!\nTente novamente:")
        area_losango()
    else:
        area = (diagonal_menor * diagonal_maior) / 2
        print(f"A área do losango é {area}{unidade}²")
    
def area_circulo():
    try:
        unidade: None = pedir_unidade()
        raio = float(input("Digite o valor do raio: "))
    except ValueError:
        print("Valor do raio precisa ser um número!\nTente novamente:")
        area_circulo()
    else:
        area = 3.14 * raio**2
        print(f"A área do círculo é {area}{unidade}²")
    
main()        
