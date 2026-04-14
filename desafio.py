#Objetivos: ler 3 notas, calcular a média e dizer se o aluno passou(média >= 7)
def main():
    try:
        print("Sistemas de notas escoteiras")

        #Solicitando 3 notas ao usuário
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))

    except ValueError:
        print("Nota invalida! Por favor, tente novamente!")
        print(".............")
        return main()
    
    else:

        #Definindo a média simples das notas
        media = (nota1 + nota2 + nota3)/3

        print(f"A média final é: {media:.1f}")

        #Verificação de aprovação do aluno
        if media >= 7:
            print("Parabéns, aluno aprovado")
        elif media >= 5:
            print("Aluno em recuperação")
        else:
            print("Aluno reprovado")

main()