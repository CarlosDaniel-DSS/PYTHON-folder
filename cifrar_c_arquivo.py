palavra = ""
palavra_criptografada = ""
lista_palavras = []
lista_criptografadas = []
valor_ascii = 0
ascii_A = ord('A')
ascii_a = ord('a')
cnt = 0

while palavra != "s":
    palavra = input("Digite uma palavra para ser criptografada (ou 's' para sair): ")
    
    if palavra != "s" and palavra != "":
        try:
            chave = int(input("Informe o valor da cifra de césamo(deslocamento): "))
            while chave > 26:
                chave = chave % 26
            
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

        except ValueError as err:
            print("Valor inválido")
            print(err)
            print("------------------------------------------------")
        else:
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