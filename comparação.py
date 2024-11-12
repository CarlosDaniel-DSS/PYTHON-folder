def main ():
    x = float(input("digite o valor de x:"))
    y = float(input("digite o valor de y:"))

    result_comparar = comparar(x,y)

    print (f"O valor de {x} é menor, maior ou igual à {y}?")
    print (result_comparar)
    
def comparar(x,y):
    if x < y:
        return "x é menor que y."
    elif x > y:
        return "x é maior que y." 
    else:
        return"x é igual à y."

main()