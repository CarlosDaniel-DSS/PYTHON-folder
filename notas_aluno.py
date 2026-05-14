nota = ''
acu = 0
cnt = 0

while cnt < 5 and nota != 's':
    nota = input("Digite uma nota ou [s] para sair: ")
    
    if nota != 's':
        try:
            acu += float(nota)
        except ValueError as err:
            print("Valor inválido")
            print(err)
        else: 
            cnt += 1
else:
    if cnt > 0:
        media = acu / cnt
        print(f"Média: {media:.2f}")
    else:
        print("Nenhuma nota válida foi digitada.")

''''
nota = ''
acu = 0
cnt = 0

while nota != 's':
    nota = input("Digite uma nota ou [s] para sair: ")

    if nota != 's':
        try:
            valor = float(nota)
            acu += valor
            cnt += 1

        except ValueError as err:
            print("Valor inválido")
            print(err)

if cnt > 0:
    media = acu / cnt
    print(f"Média: {media:.2f}")
else:
    print("Nenhuma nota foi digitada.")'''''         
            
    
#and not(n1.isnumeric()) and not(n2.isnumeric()) and not(n3.isnumeric()) and not(n4.isnumeric()) and not(n5.isnumeric()):