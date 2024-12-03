# define a funcção que recebeŕa o texto digitado
escolher = input("Digite o nome do planeta para obter informações: ") 
    
# define um dicionário para cada planeta da lista
informações_planetas = [

    # informações do planeta Mercúrio:
    {"Nome": "Mercúrio",
     "Tamanho": "Tamanho: Seu tamanho é 4.879 km de diâmetro",
     "Classificação": "Classificação: Terrestre",
     "Distância da Terra": "Distância da Terra: 108.208.130 km",
     "Peso": "Peso: 3,3022 x 10^23 kg",
     "Volume": "Volume: 6,08272 x 10^10 km³"},

    # informaçõe do planeta Vênus:
    {"Nome": "Vênus",
     "Tamanho": "Tamanho: 2.104 km de diâmetro",
     "Classificação": "Classificação: Terrestre",
     "Distância da Terra": "Distância da Terra: 108.208.930 km",
     "Peso": "Peso: 4,8695 x 10^24 kg",
     "Volume": "Volume: 9,2843 x 10^11 km³"},
 
    # informações do planeta Terra:
    {"Nome": "Terra",
     "Tamanho": "Tamanho: 12.742 km de diâmetro",
     "Classificação": "Classificação: Terrestre",
     "Distância da Terra": "Distância da Terra: 0 km",
     "Peso": "Peso: 5,9723 x 10^24 kg",
     "Volume": "Volume: 1,08321 x 10^12 km³"},

    # informações do planeta Marte:
    {"Nome": "Marte",
     "Tamanho": "Tamanho: 6.794 km de diâmetro",
     "Classificação": "Classificação: Terrestre",
     "Distância da Terra": "Distância da Terra: 227.939.200 km",
     "Peso": "Peso: 6,4185 x 10^23 kg",
     "Volume": "Volume: 1,6318 x 10^11 km³"},

    # informações do planeta Júpiter:
    {"Nome": "Júpiter",
     "Tamanho": "Tamanho: 142.984 km de diâmetro",
     "Classificação": "Classificação: Gasoso",
     "Distância da Terra": "Distância da Terra: 778.299.00 km",
     "Peso": "Peso: 1,8986 x 10^27 kg",
     "Volume": "Volume: 1,43188 x 10^15 km³"},
     
    # informações do planeta Saturno:
    {"Nome": "Saturno",
     "Tamanho": "Tamanho: 116.460 km de diâmetro",
     "Classificação": "Classificação: Gasoso",
     "Distância da Terra": "Distância da Terra: 1.426.666.400 km",
     "Peso": "Peso: 5,6846 x 10^26 kg",
     "Volume": "Volume: 8,2713 x 10^14 km³"},

    # informações do planeta Urano:
    {"Nome": "Urano",
     "Tamanho": "Tamanho: 51.118 km de diâmetro",
     "Classificação": "Classificação: Gasoso",
     "Distância da Terra": "Distância da Terra: 2.870.972.200 km",
     "Peso": "Peso: 8,6810 x 10^25 kg",
     "Volume": "Volume: 6,211 x 10^13 km³"},

    # informaçõe do planeta Netuno:
    {"Nome": "Netuno",
     "Tamanho": "Tamanho: 49.528 km de diâmetro",
     "Classificação": "Clasificação: Gasoso",
     "Distância da Terra": "Distância da Terra: 4.497.072.000 km",
     "Peso": "Peso: 1,0243 x 10^26 kg",
     "Volume": "Volume: 6,253 x 10^13 km³"},

    # informações do planeta Kleper-62f:
    {"Nome": "Kleper-62f",
     "Tamanho": "Tamanho: 1,4 vezes o da Terra",
     "Classificação": "Classificação: fora da Via Láctea",
     "Distância da Terra": "Distância da terra: 1.200 anos-luz",
     "Peso": "Peso: 2,28 vezes o da Terra",
     "Volume": "Volume: 1,61 vezes o da Terra"},

    # informações do planeta TRAPPIST-1e:
    {"Nome": "TRAPPIST-1e",
     "Tamanho": "Tamanho: 0,9 vezes o da Terra",
     "Clasificação": "Clasificação: fora da Via Láctea",
     "Distância da Terra": "Distância da Terra: 39 anos-luz",
     "Peso": "Peso: 0,8 vezes o da Terra",
     "Volume": "Volume: 0,920 vezes o da Terra"}
]
    
# printa cada item do dicionário de cada planeta da lista
for planeta in informações_planetas:
    if planeta["Nome"] in escolher:
        print(planeta["Nome"], planeta["Tamanho"], planeta["Classificação"], planeta["Distância da Terra"], planeta["Peso"], planeta["Volume"], sep = "\n")
