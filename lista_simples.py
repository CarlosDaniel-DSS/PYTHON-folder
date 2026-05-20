'''#definindo lista
lista = ["B", "D", "E"]

#inserindo valores na lista (de A a F)
lista.insert(0, "A")
lista.insert(2, "C")
lista.append("F")

#Substituindo "C" por "X"
lista[2] = "X"

# armazenando um dado d lista em uma variável

print(lista)'''

# atividade 2

'''lista = ["a", "b", "c", "d", "e", "f", "g", "h"]

abc = []
abc += lista[0]
abc += lista[1]
abc += lista[2]

print(abc)

#segunda parte
acefh = []
acefh += lista[0]
acefh += lista[2]
acefh += lista[4]
acefh += lista[7]

print(acefh)

#terceira parte

del(lista[6])
print(lista)'''

# atividade 3

lista = []
lista += "x", "y", "z"

lista.insert(0, "k")
lista.insert(1, "w")

print(lista)

lista_pop = []
lista_pop += lista.pop(2)
lista_pop += lista.pop(2)
lista_pop += lista.pop(2)

print(lista_pop)

lista_pop[0] = "X"
lista_pop[1] = "Y"
lista_pop[2] = "Z"

lista_pop.insert(0, "O")

print(lista_pop)

