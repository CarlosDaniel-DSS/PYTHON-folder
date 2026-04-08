def main():
    try:
        nascimento = int(input("Digite o seu ano de nascimento: "))
    except ValueError:
        print("Número inválido! Por favor tente novamente.")
        print("-------------------------------------------")
        main()
    else:
        idade = 2026 - nascimento
        
        if idade >= 18:
            print("Acesso liberado.")
        else:
            print("Acesso negado.")
            
main()