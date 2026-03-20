def main():
    try:
        tempo = int(input("Digite o valor em segundos: "))
    except ValueError:
        print("Valor inválido! Por favor digite um valor numérico.")
        print("---------------------------------------------------")
        main()
    else:
        dias = tempo // 86400
        resto = tempo % 86400

        horas = resto // 3600
        resto = resto % 3600

        minutos = resto // 60
        segundos = resto % 60

        print(f"{dias} dia(s), {horas} hora(s), {minutos} minuto(s), {segundos} segundo(s)") 
        print(f"O tempo é de {dias}:{horas}:{minutos}:{segundos}")
        print("---------------------------------------------------------------------------")
main()