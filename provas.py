'''
def main():
    try:
        n1 = float(input("Digite a primeira nota: "))
        p1 = int(input("Digite o peso dela: "))
        n2 = float(input("Digite a segunda nota: "))
        p2 = int(input("Digite o peso dela: "))
        n3 = float(input("Digite a terceira nota: "))
        p3 = int(input("Digite o peso dela: "))
    except ValueError:
        print("Valores inválidos! Tente novamente com números.")
        print("-----------------------------------------------")
        main()
    else:
        media_ponderada = (n1 * p1 + n2 * p2 + n3 * p3)/(p1 + p2 + p3)
        print(f"A média ponderadas das nota foi {media_ponderada:.1f}")
        
main()'''

def main():
    try:
        notas = list(map(float, input("Digite as notas: ").split()))
        pesos = list(map(int, input("Digite os pesos das notas, respectivamente: ").split()))
        
        if len(notas) != len(pesos):
            print("A quantidade de pesos não corresponde à quantidade de notas!")
            return
        
        media = sum(notas * pesos for notas, pesos in zip(notas, pesos)) / sum(pesos)
        
        print(f"A media ponderada é {media:.1f}")
        
    except ValueError:
        print("Valores inválidos! Tente novamente com números.")
        print("-----------------------------------------------")
        main()
    
main()