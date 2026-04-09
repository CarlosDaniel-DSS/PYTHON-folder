def escada_main():
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Idade inválida! Por favor, tente novamente.")
        print("-------------------------------------------")
        main()
    else:
        if 0 <= idade < 12:
            print("Criança.")
        else:
            if idade < 18:
                print("Adolescente")
            else:
                if idade < 30:
                    print("Jovem")
                else:
                    if idade < 60:
                        print("Adulto")
                    else:
                        if idade >= 60:
                            print("Idoso")
                        else:
                            print("Não humano")

def main():
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Idade inválida! Por favor, tente novamente.")
        print("-------------------------------------------")
        main()
    else:
        if 0 <= idade < 12:
            print("Criança.")
        elif idade < 18:
            print("Adolescente")
        elif idade < 30:
                print("Jovem")
        elif idade < 60:
            print("Adulto")
        elif idade >= 60:
            print("Idoso")
        else:
            print("Não humano")
                            
escada_main()
main()