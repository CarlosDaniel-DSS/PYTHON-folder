def main ():
    # Solicita um número de entrada
    num = int(input("Digite número:"))
    
    # Verifica se é par
    if verificar_par(num):
        print (f"{num} é par")
    else:
        print (f"{num} é ímpar")    
    
def verificar_par(num):
    return num % 2 == 0

main()