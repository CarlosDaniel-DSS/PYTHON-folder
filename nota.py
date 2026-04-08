nota = float(input("Digite uma nota: "))

#Somente "parabéns"
if nota >=7 and nota >= 9:
    print("Parabéns")

#Somente "aprovado"
if nota >=7 and not(nota >=9):
    print("Aprovado")

#Somente "recuperação"
if not(nota >=7) and nota >=4:
    print("Recuperação")

#Somente "reprovado"
if not(nota >=7) and not(nota >=4):
    print("Reprovado")
    
    
