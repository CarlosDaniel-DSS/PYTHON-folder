def main(): 
    nota = float(input("Nota do estudante:"))

    result_nota = verificar_nota(nota)

    print(f"A sua nota {nota} é {result_nota}.")

def verificar_nota(nota):
    if 0 <= nota < 10:
        return "F"
    elif 9 < nota < 20:
        return "C-"
    elif 19 < nota < 30:
        return "C"
    elif 29 < nota < 40:
        return "C+"
    elif 39 < nota < 50:
        return "B-"
    elif 49 < nota < 60:
        return "B"
    elif 59 < nota < 70:
        return "B+"
    elif 69 < nota < 80:
        return "A-"
    elif 79 < nota < 90:
        return "A"
    else: 
        if 89 < nota <= 100:
            return "A+"

main()