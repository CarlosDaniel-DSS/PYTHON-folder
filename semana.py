#Com lista
'''def main():
    try:
        dia = int(input("Digite o número do dia da semana: "))
        if dia not in [1, 2, 3, 4, 5, 6, 7]:
            return main()
        else:
            pass
    except ValueError:
        print("Valor inválido! Por favor, tente novamente.")
        print("-------------------------------------------")
        return main()
    else:       
        if 1:
            print("Domingo")
        case 2:
            print("Segunda")
        case 3:
            print("Terça")
        case 4:
            print("Quarta")
        case 5:
            print("Quinta")
        case 6:
            print("Sexta")
        else:
            print("Sábado")
            
main()'''

#Sem lista
'''def main():
    try:
        dia = int(input("Digite o número do dia da semana: "))
    except ValueError:
        print("Valor inválido! Por favor, tente novamente.")
        print("-------------------------------------------")
        return main()
    else:       
        if 1:
            print("Domingo")
        case 2:
            print("Segunda")
        case 3:
            print("Terça")
        case 4:
            print("Quarta")
        case 5:
            print("Quinta")
        case 6:
            print("Sexta")
        case 7:
            print("Sábado")
        else:
            print("Não existe")

main()'''
            
'''#Com case
def main():
    try:
        dia = int(input("Digite o número do dia da semana: "))
        if dia not in [1, 2, 3, 4, 5, 6, 7]:
            return main()
        else:
            pass
    except ValueError:
        print("Valor inválido! Por favor, tente novamente.")
        print("-------------------------------------------")
        return main()
    else:       
        match dia:
            case 1:
                print("Domingo")
            case 2:
                print("Segunda")
            case 3:
                print("Terça")
            case 4:
                print("Quarta")
            case 5:
                print("Quinta")
            case 6:
                print("Sexta")
            case _:
                print("Sábado")
                print("-----------------------------------")

main()'''

#Calculadora básica             
def main():
    try:
        n1 = float(input("Digite o primeiro número da operação: "))
         
        #Verificação dooperador com lista
        '''
        op = input("Digite o perador da conta('-'; '+'; '*' ou '/'): ")
        if operador not in ["-", "+", "*", "/"]:
            print("Operador inválido! Por favor tente novamente.")
            print("---------------------------------------------")
            return main()
        else:
            pass
        '''
            
        #Verificação do operador sem lista
        op = input("Digite o perador da conta('-'; '+'; '*' ou '/'): ")
        if op == "+" or op == "-" or op == "*" or op == "/":
            pass
        else:
            print("Operador inválido! Por favor tente novamente.")
            print("---------------------------------------------")
            return main()
        
        n2 = float(input("Digite o segundo número da operação: "))
        
    except ValueError:
        print("Valor inválido! Por favor, tente novamente.")
        print("-------------------------------------------")
        return main()
    else:       
        match op:
            case "+":
                print(f"O resultado da soma é {(n1 + n2):.2f}")
            case "-":
                print(f"O resultado da subtração é {(n1 - n2):.2f}")
            case "*":
                print(f"O resultado da multiplicação é {(n1 * n2):.2f}")
            case "/":
                print(f"O resultado da divisão é {(n1 / n2):.2f}")
                
        print("----------------------------------------")
main()