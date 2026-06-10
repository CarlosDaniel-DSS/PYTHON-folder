
d_lista_letras = []
palavra_criptografada = []
palavra = ""          # Aqui o usuário digita a string de números (ex: 079105)
d_palavra_ascii = ""    # Armazenará a palavra reconstruída
d_valor_ascii = 0       # Armazenará o bloco numérico atual convertido em int
d_cnt = 0

while palavra != "s":
    palavra = input("Digite os números ASCII (3 dígitos por letra) ou 's' para sair: ")
    
    if palavra != "s":
        try:
            # Garante que estamos processando apenas os dígitos numéricos digitados
            numeros_limpos = ""
            for caractere in palavra:
                if caractere.isdigit():
                    numeros_limpos += caractere

            # Fatiando a string de números de 3 em 3 usando um while manual (sem range)
            posicao = 0
            while posicao < len(numeros_limpos):
                pedaco = numeros_limpos[posicao : posicao + 3]
                
                # Só processa se o bloco tiver exatamente 3 dígitos
                if len(pedaco) == 3:
                    d_valor_ascii = int(pedaco)
                    letra = chr(d_valor_ascii)
                    
                    # CORREÇÃO DO PRINT INDIVIDUAL: Registra cada letra e seu respectivo código
                    d_lista_letras.append(f"ASCII: {pedaco} --> Caractere: '{letra}'\n")
                    
                    # Junta a letra na palavra que está sendo reconstruída
                    d_palavra_ascii += letra
                
                posicao += 3 # Avança o cursor para o próximo bloco de 3
                
        except ValueError as err:
            print("Não foi possível converter os números para palavra (valor inválido).")
            print(err)
            print("---------------------------------------------------------")
        else:
            # Se uma palavra válida foi gerada, adiciona na lista final
            if d_palavra_ascii != "":
                palavra_criptografada.append(d_palavra_ascii)
                d_palavra_ascii = ""
                d_cnt += 1
            else:
                print("Nenhum bloco válido de 3 dígitos foi encontrado nesta linha.")
else:
    if d_cnt > 0:
        # Exibe o histórico de conversão letra por letra
        print("\n--- HISTÓRICO DE CONVERSÃO ---")
        for registro in d_lista_letras:
            print(registro, end="")
            
        print("------------------------------")
        # Exibe a lista final com as palavras reconstruídas
        print(f"PALAVRAS GERADAS: {palavra_criptografada}")
    else:
        print("Nenhuma sequência de números válida foi digitada.")

'''
numero = ""
cnt1 = 0
cnt2 = 0
lista_numeros = []
lista_palavras = []

#traduzir de ascii pra palavra'''