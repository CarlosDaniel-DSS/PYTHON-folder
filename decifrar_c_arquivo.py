chave = int(input("Digite a chave para descriptografar a mensagem: "))
while chave > 26:
    chave = chave % 26

arquivo = open("/home/carlosdaniel/PYTHON-folder-main/terceiro-ano/arquivos/mensagem.txt", "r")
criptografada = arquivo.read()
arquivo.close()

palavra_decifrada = ""

for letra in criptografada:
    #Concertar letra maíuscula #####
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

    palavra_decifrada += nova_letra
    
print(f"Mensagem original: {palavra_decifrada}")

#Reescrevendo a mensagem original no arquivo
for letra in criptografada:
    del(letra)
else:
    arquivo = open("/home/carlosdaniel/PYTHON-folder-main/terceiro-ano/arquivos/mensagem.txt", "r+")
    arquivo.write(f"\n{palavra_decifrada}")
    arquivo.close()
