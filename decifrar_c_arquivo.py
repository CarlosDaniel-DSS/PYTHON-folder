'''
palavra = ""
palavra_descriptografada = ""
lista_palavras = []
valor_ascii = 0
ascii_A = ord('A')
ascii_a = ord('a')


arquivo = open("/home/carlosdaniel/PYTHON-folder-main/terceiro-ano/arquivos/mensagem.txt", "r+")

for linha in arquivo:
    for letra in linha:
        mensagem += letra
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

#corrigir
'''

chave = int(input("Digite a chave pa1ra descriptografar a mensagem"))

arquivo = open("/home/carlosdaniel/PYTHON-folder-main/terceiro-ano/arquivos/mensagem.txt", "r")
criptografada = arquivo.read()
arquivo.close()

ascii_A = ord('A')
ascii_a = ord('a')
palavra_decifrada = ""

for letra in criptografada:
    if 'A' <= letra <= 'Z':
        nova_letra = chr((ord(letra) - ord('A') - chave) % 26 + ord('A'))

    # Mantém letras minúsculas
    elif 'a' <= letra <= 'z':
        nova_letra = chr((ord(letra) - ord('a') - chave) % 26 + ord('a'))
        
    # Mantém caracteres especiais e números
    else:
        nova_letra = letra

    palavra_decifrada += nova_letra
    

print(f"Mensagem original: {palavra_decifrada}")