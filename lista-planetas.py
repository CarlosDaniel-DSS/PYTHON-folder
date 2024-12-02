# define a funcção que recebeŕa o texto digitado
escolher = input("Digite o nome do planeta para obter informações: ") 
    
# define um dicionŕio para cada planeta da lista
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
]
    
# printa cada item do dicionário de cada planeta da lista
for planeta in informações_planetas:
    if planeta["Nome"] in escolher:
        print(planeta["Nome"], planeta["Tamanho"], planeta["Classificação"], planeta["Distância da Terra"], planeta["Peso"], planeta["Volume"], sep = "\n")