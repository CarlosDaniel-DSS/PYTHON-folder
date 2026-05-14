idade = ""
tentativas = 0

while not(idade.isnumeric()) and tentativas < 3:
    idade = input("Digite sua idade: ")
    tentativas += 1
else:
    if idade.isnumeric():
        print(f"Sua idade é {idade} anos. Você tentou [{tentativas}] vezes")
    else:
        print(f"Erro\n[{tentativas}] tentativas.")
    
    
