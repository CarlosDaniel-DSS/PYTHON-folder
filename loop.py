'''# loop com fim:
x = 1

while x <= 4:
    print (x, "Atumalaka")
    x += 1

# fórmula do loop ininito: [while true: print("blá, blá, blá")]

# forma com lista:
for x in range(4):
    print (x, "Atumalaka")'''

'''# loop com fim:
x = 1

while x <= 4:
    print (x, "Atumalaka")
    x += 1

# fórmula do loop ininito: [while true: print("blá, blá, blá")]

# forma com lista:
for x in range(4):
    print (x, "Atumalaka")'''

def main():
    escolha_loop = input("Digite o tipo de loop (finito ou infinito)")
    escolher_tipo_de_loop(escolha_loop)

def escolher_tipo_de_loop(escolha_loop):
    if escolha_loop == "finito":
        x = int(input("Digite o valor do loop: "))
        for _ in range(x):
            print("Eu sou o melhor!")
    else:
            while True:
                print("Eu sou o melhor!")

main()
