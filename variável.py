def main():
    while True:
        try:
            valor = float(input("digite um número decimal: "))
        except ValueError as erro:
            print("Valor inválido! tente novamente.")
        else:
            print("Você digitou: ", valor)
            break
            
        
main()
   
            
            
            