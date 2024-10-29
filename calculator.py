# pegar valores da conta
x = float(input("digite o primeio número:")) 
y = float(input("digite o segundo número:"))
z = float(input("digite o terceiro número"))
# Calcula e exibe o resultado
resultado = (x + y) * z # expressão que será calculada
resultado = f"{resultado:_.2f}" # definindo o número de casas decimais e o separador de milhar por "_"
resultado = resultado.replace(".",",").replace("_",".") # mudando os separadores do modelo americano para o brasileiro
print(f"O quadrado da soma de {x} mais {y} elevado à {z} é {resultado}") 
