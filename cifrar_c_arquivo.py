#Cifrando mensagens com arquivo e cifra de césar (deslocamento com chave)

'''def criptografia_de_mensagens():
    
    palavra = ""
    palavra_criptografada = ""
    lista_palavras = []
    lista_criptografadas = []
    valor_ascii = 0
    ascii_A = ord('A')
    ascii_a = ord('a')
    cnt = 0
    
    #Pedindo a chave da criptografia de todas as palvras
    try:
        chave = int(input("Informe o valor da cifra de césamo(deslocamento) das palavras: "))
        while chave > 26:
            chave = chave % 26
    except ValueError as err:
                print("Valor inválido")
                print(err)
                print("------------------------------------------------")
    
    #Criptografando todas as palavras que o usuário digitar    
    while palavra != "s":
        palavra = input("Digite uma palavra para ser criptografada (ou 's' para sair): ")
        
        if palavra != "s" and palavra != "":
                
                for letra in palavra:
                    # Mantém letras maiúsuclas
                    if 'A' <= letra <= 'Z':
                        nova_letra = chr((ord(letra) - ord('A') + chave) % 26 + ord('A'))

                    # Mantém letras minúsculas
                    elif 'a' <= letra <= 'z':
                        nova_letra = chr((ord(letra) - ord('a') + chave) % 26 + ord('a'))
                        
                    # Mantém caracteres especiais e números
                    else:
                        nova_letra = letra

                    palavra_criptografada += nova_letra
        
                lista_palavras.append(palavra)
                lista_criptografadas.append(palavra_criptografada)
                palavra_criptografada = ""
                
                cnt += 1
        else:
            if palavra == "":
                print("Nenhuma palavra foi digitada.")
    else:
        if cnt > 0:
            print(f"\nOriginal: {lista_palavras}")
            
            #Colocando a criptografia no arquivo
            arquivo = open("/home/carlosdaniel/PYTHON-folder-main/terceiro-ano/arquivos/mensagem.txt", "w")
            arquivo.close()
            
            arquivo = open("/home/carlosdaniel/PYTHON-folder-main/terceiro-ano/arquivos/mensagem.txt", "r+")
            for linha in arquivo:
                pass
            
            for palavra in lista_criptografadas:
                arquivo.write(f"\n{palavra}")
            
            arquivo.close()
criptografia_de_mensagens()'''

# Cifrando com cifra de césar(deslocamento com chave) e escrevendo em um arquivo
def criptografia_de_mensagens():
    
    palavra = ""
    palavra_criptografada = ""
    lista_palavras = []
    lista_criptografadas = []
    cnt = 0
    
    #Pedindo a chave da criptografia de todas as palvras
    try:
        chave = int(input("Informe o valor da cifra de césamo(deslocamento) das palavras: "))
        while chave > 26:
            chave = chave % 26
    except ValueError as err:
                print("Valor inválido")
                print(err)
                print("------------------------------------------------")
    
    #Criptografando todas as palavras que o usuário digitar    
    while palavra != "s":
        palavra = input("Digite uma palavra para ser criptografada (ou 's' para sair): ")
        
        if palavra != "s" and palavra != "":
                
                for letra in palavra:
                    # Mantém letras maiúsuclas
                    if 'A' <= letra <= 'Z':
                        nova_letra = (ord(letra) - ord('A') + chave) % 26 
                        nova_letra = chr(90 - nova_letra)

                    # Mantém letras minúsculas
                    elif 'a' <= letra <= 'z':
                        nova_letra = (ord(letra) - ord('a') + chave) % 26
                        nova_letra = chr(122 - nova_letra)
                        
                    # Mantém caracteres especiais e números
                    else:
                        nova_letra = letra

                    palavra_criptografada += nova_letra
        
                lista_palavras.append(palavra)
                lista_criptografadas.append(palavra_criptografada)
                palavra_criptografada = ""
                
                cnt += 1
        else:
            if palavra == "":
                print("Nenhuma palavra foi digitada.")
    else:
        if cnt > 0:
            print(f"\nOriginal: {lista_palavras}")
            
            #Colocando a criptografia no arquivo
            arquivo = open("/home/carlosdaniel/PYTHON-folder-main/terceiro-ano/arquivos/mensagem.txt", "w")
            arquivo.close()
            
            arquivo = open("/home/carlosdaniel/PYTHON-folder-main/terceiro-ano/arquivos/mensagem.txt", "r+")
            for linha in arquivo:
                pass
            
            for palavra in lista_criptografadas:
                arquivo.write(f"\n{palavra}")
            
            arquivo.close()
criptografia_de_mensagens()
