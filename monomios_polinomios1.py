def to_superindice(numero):
    superi = {"0":"⁰", "1":"¹", "2":"²", "3":"³", "4":"⁴", "5":"⁵",
              "6":"⁶", "7":"⁷", "8":"⁸", "9":"⁹", "-":"⁻"}
    return ''.join(superi[c] for c in str(numero))

def imprimir_termino(coef, vars_con_exp):
    if coef == 0:
        return ""
    
    coef_str = str(int(coef)) if coef.is_integer() else str(coef)
    if coef == 1 and vars_con_exp:
        coef_str = ""
    elif coef == -1 and vars_con_exp:
        coef_str = "-"

    partes = [coef_str]
    for var, exp in vars_con_exp.items():
        if exp == 0:
            continue
        elif exp == 1:
            partes.append(f"{var}")
        else:
            partes.append(f"{var}{to_superindice(exp)}")
    return "".join(partes)

def ingresar_expresion():
    n = int(input("¿Cuántos términos tendrá la expresión? "))
    expresion = []

    for i in range(n):
        print(f"\nTérmino {i+1}:")
        coef = float(input("  Coeficiente: "))
        num_vars = int(input("  ¿Cuántas variables tiene este término? "))
        vars_con_exp = {}

        for j in range(num_vars):
            var = input(f"    Variable #{j+1} (ej. x, y, z): ").strip().lower()
            exp = int(input(f"    Exponente de {var}: "))
            vars_con_exp[var] = exp

        expresion.append((coef, vars_con_exp))

    return expresion

def imprimir_expresion(expresion):
    partes = []
    for coef, vars_con_exp in expresion:
        term = imprimir_termino(coef, vars_con_exp)
        if term:
            partes.append(term)
    return " + ".join(partes).replace("+ -", "- ")

def main():
    print("=== CONSTRUCTOR DE EXPRESIONES ALGEBRAICAS MULTIVARIABLES ===")
    expr = ingresar_expresion()
    print("\n🔹 Representación:")
    print(" ", imprimir_expresion(expr))

if __name__ == "__main__":
    main()
