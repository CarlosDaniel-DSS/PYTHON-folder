escolher = input("Digite o nome do planeta para obter informações: ") 

informações_planetas = [
    {"Nome": "Nome: Seu nome é Mercúrio",
    "Tamanho": "Tamanho:vSeu tamanho é 4.879 km de diâmetro",
    "Classificação": "Classificação: Terrestre",
    "Distância da Terra": "Distância da Terra: 108.208.130 km",
    "Peso": "Peso: 3,3022 x 10^23 kg",
    "Volume": "Volume: 6,08272 x 10^10 km³"},

    {"Nome": "Vênus",
    "Tamanho": "12.104 km de diâmetro",
    "Classificação": "Terrestre",
    "Distância da Terra": "108.208.930 km",
    "Peso": "4,8695 x 10^24 kg",
    "Volume": "9,2843 x 10^11 km³"},
]

for planeta in informações_planetas:
    if planeta in escolher:
        print(planeta["Nome"], planeta["Tamanho"], planeta["Classificação"], planeta["Distância da Terra"], planeta["Peso"], planeta["Volume"], sep = "\n")
