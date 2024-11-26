# lista normal:
'''estudantes = ["Xaulin matador de porco", "João do pneu", "enzoprogamer157", "20pegar70fugir", "AtumalakaRGB"]
casas = [98, 126, 205, 18, 76]

for e in range(len(estudantes)):
    print (e + 1, estudantes[e], casa[e])'''

# dicionário:
'''estudantes = {
    "Xaulin matador de porco": "98",
    "João do pneu": "126",
    "enzoprogamer157": "205",
    "20pegar70fugir": "18",
    "AtumalakaRGB": "76"}

for estudante in estudantes:
    print(estudante, estudantes[estudante], sep = ", ")'''

# cada estudante tem o seu próprio dicionário
estudantes = [
    {"nome": "Carlos", "casa": "780", "cidade": "Boca da Mata"},
    {"nome": "Marcelo","casa": "199", "cidade": "Boca da Mata"},
    {"nome": "Luna", "casa": "506", "cidade": "Maceió"},
    {"nome": "Jackson", "casa": "654", "cidade": "Marechal Deodoro"},
]

# mostra os elementos dos dicionários de cada estudante
for estudante in estudantes:
    print(estudante["nome"], estudante["casa"], estudante ["cidade"], sep= ", ")