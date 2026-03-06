def main():
    
    opcoes = [
    "1 - Celsius para Kelvin",
    "2 - Kelvin para Celsius",
    "3 - Celsius para Fahrenheit",
    "4 - Fahrenheit para Celsius",
    "5 - Kelvin para Fahrenheit",
    "6 - Fahrenheit para Kelvin"
    ]
    
    for opcao in opcoes:
        print(opcao)


    escolher = int(input("Escolha o número da respectiva opção de conversão desejada: "))
    
    if escolher == 1:
        um()
    elif escolher == 2:
        dois()
    elif escolher == 3:
        tres()
    elif escolher == 4:
        quatro()
    elif escolher == 5:
        cinco()
    elif escolher == 6:
        seis()
    else:
        print("Escolha novamente.")
        main()
        
            

def um():
    celsius = float(input("Digite o valor de celsius: "))
    kelvin = celsius + 273.15
    print(f"A conversão de celsius ({celsius}) para kelvin é {kelvin}")
    
def dois():
    kelvin = float(input("Digite o valor de kelvin: "))
    celsius = kelvin - 273.15
    print(f"A conversão de kelvin ({kelvin}) para celsius é {celsius}")
    
def tres():
    celsius = float(input("Digite o valor de celsius: "))
    fahrenheit = celsius / (9/5) + 32
    print (f"A conversão de celsius ({celsius}) para fahrenheit {fahrenheit}")
    
def quatro():
    fahrenheit = float(input("Digite o valor de fahrenheit: "))
    celsius = (fahrenheit - 32) * (5/9)
    print (f"A conversão de fahrenheit ({fahrenheit}) para celsius é {celsius}")
    
def cinco():
    kelvin = float(input("Digite o valor de kelvin: "))
    fahrenheit = (kelvin - 273.15) * (9/5) + 32
    print(f"A conversão de fahrenheit({fahrenheit}) para kelvin é {kelvin}")
    
def seis():
    fahrenheit = float(input("Digite o valor de fahrenheit: "))
    kelvin = (fahrenheit - 32) * (5/9) + 273.15
    print(f"A conversão de fahrenheit {fahrenheit} para kelvin é {kelvin}")
    
main()