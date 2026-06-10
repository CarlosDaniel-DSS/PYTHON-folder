lista_letras = []
valor_ascii_final = []
palavra = ""
palavra_ascii = ""
palavra_criptografada = []
valor_ascii = 0
cnt = 0

while palavra != "s":
    palavra = input("Digite uma palavra para ser convertida em ASCII e criptografada (ou 's' para sair): ")
    
    if palavra != "s" and palavra != "":
        try:
            #Entrada de dado da chave criptográfica
            chave = int(input("Digite um número para ser o deslocamento da Cifra de César: "))
            if chave > 26:
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
            valor_ascii_final.append(palavra_ascii)
            palavra_ascii = ""
            
            cnt += 1
    else: 
        if palavra == "":
            print("Nada foi digitado")  
            
else:
    #Printando conversões das letras pra ascii e a palavra final em ascii 
    if cnt > 0 and palavra != "":
        print("\n--- HISTÓRICO DE CONVERSÃO ---")
        for registro in lista_letras:
            print(registro, end="")
        print("------------------------------")
        print(f"VALOR ASCII DA PALAVRA: {valor_ascii_final}")
    else:
        print("Nenhuma palavra foi digitada")