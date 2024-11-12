def main():
    nome_personagem = input("digite nome o personagem:")
    
    result = verificar_casa(nome_personagem)

    print (f"A casa de(a) {nome_personagem} é {result}.")

# Concertar depois (sempre dá Grifinória)
def verificar_casa(nome_personagem):
     if nome_personagem == "Harry Poter" or "Hermione Granger" or "Rony Weasley":
         return "Grifinória"
     elif nome_personagem == "Draco Malfoy":
         return "Sonserina"
     elif nome_personagem == "Luna Lovegood":
         return "Corvinal"   
     elif nome_personagem == "Cedric Diggory":
        return "Lufa-Lufa"
     else:
         return "none"   
    
main()