lista_letras = []
valores_ascii_finais = []
palavra = ""
palavra_ascii = ""
palavra_criptografada = []
valor_ascii = 0
cnt = 0

#Variáveis da descriptografia
d_lista_letras = []
d_palavra_ascii = ""    
d_valor_ascii = 0       
d_cnt = 0

while palavra != "s":
    palavra = input("Digite uma palavra para ser convertida em ASCII e criptografada (ou 's' para sair): ")
    
    if palavra != "s" and palavra != "":
        try:
            #Entrada de dado da chave criptográfica
            chave = int(input("Digite um número para ser o deslocamento da Cifra de César: "))
            while chave > 26:
                chave = chave % 26
            
            #Convertendo cada letra da palavra para valor ASCII
            for letra in palavra:
                valor_ascii = (str(ord(letra)))
                
                #Verificando se a conversão de cada letra para ASCII possui menos que 3 digitos (se sim, modificando ele)
                if len(valor_ascii) < 3:
                    valor_ascii = valor_ascii.zfill(3)
                
                #Aplicando a chave no valor_ascii 
                valor_ascii = int(valor_ascii) + chave
                    
                #Juntando o valor ascii de cada letra da palavra em um elemento
                palavra_ascii += str(valor_ascii)
                
        except ValueError as err:
            print("Não foi possível converter a palavra para ascci (valor inválido).")
            print(err)
            print("---------------------------------------------------------")
        else:
            #Armazenando cada letra de cada palavra e seus valores ascii correspondentes em uma lista
            lista_letras.append(f"Caractere: '{letra}' --> ASCII: {valor_ascii}\n")
            
            #Adicionando a palavra ascii para a lista final e redefinindo 'palavra_ascii'   
            valores_ascii_finais.append(palavra_ascii)
            palavra_ascii = ""
            
            cnt += 1
    else: 
        if palavra == "":
            print("Nada foi digitado")  
                
else:
    '''
    if cnt > 0:
        print(lista_letras)
        print(f"VALORES ASCII: {valores_ascii_finais}")
    else:
        print("Nenhuma palavra foi digitada")'''
    
    #Printando conversões das letras pra ascii e a palavra final em ascii 
    if cnt > 0 and palavra != "":
        print("\n--- HISTÓRICO DE CONVERSÃO ---")
        for registro in lista_letras:
            print(registro, end="")
        print("------------------------------")
        print(f"VALOR ASCII DA PALAVRA: {valores_ascii_finais}")
    else:
        print("Nenhuma palavra foi digitada")
    
for palavra in valores_ascii_finais:
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