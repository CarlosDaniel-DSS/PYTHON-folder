'''def calculadora ():
    expressão = input("Digite a expressão: ")
    try:
        resultado = eval(expressão)
        print(f"Resultado: {resultado}")
    except Exception as e:
        print("Error {e}")
    
calculadora ()'''


# define que a a variável "expresão" será o que foi digitado.
def calculadora ():
    expressão = input("Digite a expressão matemática: ")

    # define que cada operador será atibuído à sua respectiva função.
    operações = {
    "+": adição,
    "-": subtração,
    "*": multiplicação,
    "/": divisão,
    }

    '''define que, para cada operador dentro da lista de operações, n1 e n2 receberão o operador da expressão, 
    poderão ser digitados com decimais e apresenta o resultado da expressão'''
    for operador in operações:
        if operador in expressão:
            try:
                n1, n2 = expressão.split(operador)
                n1, n2 = float(n1), float(n2)
                print(f"Resultado: {operações[operador](n1, n2)}") 
                break
            except ValueError:
                pass
            else:
                print("Error: operação inválida!")    
            

# define cada uma das operações aceitas no calculo da expresão.
def adição (n1, n2):
    return n1 + n2
def subtração (n1, n2):
    return n1 - n2
def multiplicação (n1, n2):
    return n1 * n2
def divisão (n1, n2):
    if n2 == 0:
        return "Error: Divisão por zero!"
    else
        return n1 / n2


calculadora()
