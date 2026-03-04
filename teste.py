
'''
#questão 7: 
bool(0) vai ser "false", enquanto bool('0') vai ser True
'''

'''
#questão 8:
x = "5.67"
x = float(x)
x = int(x)

print(x)'''


'''#questão 9:
def main():
    while True:
        try:
            n1 = float(input("Digite a primeira nota: ").replace(',','.'))
            n2 = float(input("Digite a segunda nota: ").replace(',','.'))
            n3 = float(input("Digite a terceiranota: ").replace(',','.'))
            n4 = float(input("Digite a quarta nota: ").replace(',','.'))
        except ValueError as erro:
            print("Valor inválido! tente novamente.")
        else:
             media = (n1 + n2 + n3 + n4)/4
             print(f"A média é {media}")
             break
               
main()'''


'''

#questão 10:,

x =  3.15
x = str(x)
x = x.split(x)
print(x)

#ou

x = float(x) - int(x)
print(x)

x = int(x)
print(x)'''
