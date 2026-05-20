'''lista = ["a", "b", "c", "d", "e", "f", "g", "h"]

lista_maiuscula = [letra.upper() for letra in lista]

a_h = ""
for letra in lista_maiuscula:
    a_h += letra
else:
    print(a_h)'''
    
'''
lista = ["a", "b", "c", "d", "e", "f", "g", "h"]
cnt = 1
a_h = ""

while cnt < len(lista):
    lista_maiuscula = [letra.upper() for letra in lista]
    cnt += 1
else:
    for letra in lista_maiuscula:
        a_h += letra
    else: 
        print(a_h)
'''

#Consumindo lista

'''lista = ["a", "b", "c", "d", "e", "f", "g", "h"]
popai = []

for letra in lista:
    print(letra)
    
for letra in lista:
    popai += lista.pop(letra)
else:
    print(popai)'''
    
'''ista = ["a", "b", "c", "d", "e", "f", "g", "h"]
str = ""
cnt = 0
leng = len(lista)

while cnt < leng:
    letra = lista.pop(0)
    str += letra.upper()
    cnt += 1
else:
    print(str)'''
    
# Fatiando lista
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alfabeto[1:10:2])