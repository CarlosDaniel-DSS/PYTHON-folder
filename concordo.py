# define a função principal
def main ():
    resposta_do_usuário = input("Você concorda?")

    # recebe a verificação da resposta do usuário
    resultado = verificar_resposta(resposta_do_usuário)

    # exibe o resultado
    print (f"Eu {resultado}")

# função que define a verificação da resposta e retorna um argumento para "resultado"
def verificar_resposta(resposta_do_usuário):
    if resposta_do_usuário == "Sim" or resposta_do_usuário == "sim" or resposta_do_usuário == "S" or resposta_do_usuário == "s":
        return "concordo"
    elif resposta_do_usuário == "Não" or resposta_do_usuário == "não" or resposta_do_usuário == "N" or resposta_do_usuário == "n":
        return "não concordo"
    else:
        return "Resposta inválida. Por favor, tente novamente."
    
main()