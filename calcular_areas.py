def main():
    
    escolher = input("Escolha uma figura para calcular sua área (triangulo, quadrado, retangulo, trapezio, losango ou circulo):")
    
    if escolher == "triangulo":
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
        print("Escolha novamente.")
        main()
        
            

def area_triangulo():
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))
    area = base * altura /2
    print(f"A área do triângulo é {area}")
    
def area_quadrado():
    base = float(input("Digite o valor da base: "))
    area = base ** 2
    print(f"A área do quadrado é {area}")
    
def area_retangulo():
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))
    area = base * altura 
    print(f"A área do retângulo é {area}")
    
def area_trapezio():
    base_menor = float(input("Digite o valor da base menor: "))
    base_maior = float(input("Digite o valor da base maior: "))
    altura = float(input("Digite o valor da altura"))
    area = (base_menor + base_maior) * altura / 2
    print(f"A área do trapézio é {area}")
    
def area_losango():
    diagonal_menor = float(input("Digite o valor da diagonal menor: "))
    diagonal_maior = float(input("Digite o valor da diagonal maior: "))
    area = (diagonal_menor * diagonal_maior) / 2
    print(f"A área do losango é {area}")
    
def area_circulo():
    raio = float(input("Digite o valor do raio: "))
    area = 3.14 * raio**2
    print(f"A área do círculo é {area}")
    
main()
            
            
    
        