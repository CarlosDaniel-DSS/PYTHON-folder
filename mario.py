'''def linha():
    largura = int(input("Digite a largura da linha: "))
    print("=" * largura)
        
def coluna():
    altura = int(input("Digite a altura da coluna: "))
    for _ in range(altura):
        print("||")
        
def bloco():
    tamanho = int(input("Digite o tamanho do bloco: "))
    for _ in range(tamanho):
        print("#" * tamanho)

escolha = input("Escolha a função que irá usar (linha, coluna ou bloco): ")

if escolha == "linha":
    linha()
elif escolha == "coluna":
    coluna()
elif escolha == "bloco":
    bloco()
else:
    print("Opção inválida")'''

def main():
    escolha = input("Escolha a função que irá usar (linha, coluna ou bloco): ")

    if escolha == "linha":
    linha()
    elif escolha == "coluna":
    coluna()
    elif escolha == "bloco":
    bloco()
    else:
    print("Opção inválida")

def linha():
    largura = int(input("Digite a largura da linha: "))
    print("=" * largura)
        
def coluna():
    altura = int(input("Digite a altura da coluna: "))
    for _ in range(altura):
        print("||")
        
def bloco():
    tamanho = int(input("Digite o tamanho do bloco: "))
    for _ in range(tamanho):
        print("#" * tamanho)