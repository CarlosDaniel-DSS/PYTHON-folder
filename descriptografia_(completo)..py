palavra = ""
palavra_descriptografada = ""
lista_palavras = []
valor_ascii = 0
ascii_A = ord('A')
ascii_a = ord('a')
cnt = 0

while palavra != "s":
    palavra = input("Digite uma palavra para ser descriptografada (ou 's' para sair): ")

    if palavra != "s" and palavra != "":
        try:
            chave = int(input("Informe o valor da cifra de césar (deslocamento): "))
            while chave > 26:
                chave = chave % 26

            for letra in palavra:
                # Conversão da letra para ASCII
                valor_ascii = ord(letra)

                # Mantém letras maiúsculas
                if letra >= 'A' and letra <= 'Z':
                    nova_letra = ((valor_ascii - ascii_A - chave) % 26) + ascii_A
                    palavra_descriptografada += chr(nova_letra)

                # Mantém letras minúsculas
                elif letra >= 'a' and letra <= 'z':
                    nova_letra = ((valor_ascii - ascii_a - chave) % 26) + ascii_a
                    palavra_descriptografada += chr(nova_letra)

                # Mantém caracteres especiais
                else:
                    palavra_descriptografada += letra
        except ValueError as err:
            print("Valor inválido")
            print(err)
            print("------------------------------------------------")
        else:
            lista_palavras.append(palavra_descriptografada)
            palavra_descriptografada = ""
            cnt += 1
    else:
        if palavra == "":
            print("Nenhuma palavra foi digitada.")
else:
    if cnt > 0:
        print(f"\nDescriptografada: {lista_palavras}")