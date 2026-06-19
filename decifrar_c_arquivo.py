chave = int(input("Digite a chave pa1ra descriptografar a mensagem"))
while chave > 26:
    chave = chave % 26

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
