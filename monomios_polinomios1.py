from collections import defaultdict

def to_superindice(numero):
    superi = {"0":"⁰", "1":"¹", "2":"²", "3":"³", "4":"⁴", "5":"⁵",
              "6":"⁶", "7":"⁷", "8":"⁸", "9":"⁹", "-":"⁻"}
    return ''.join(superi[c] for c in str(numero))

def imprimir_termino_descompuesto(coef, vars_con_exp):
    if coef == 0:
        return ""
    
    coef_str = str(int(coef)) if coef.is_integer() else str(coef)
    variables = []

    for var in sorted(vars_con_exp):
        exp = vars_con_exp[var]
        if exp == 0:
            continue
        elif exp == 1:
            variables.append(f"{var}")
        else:
            variables.append(f"{var}{to_superindice(exp)}")

    # Si hay más de una variable, separar visualmente como en el cole
    if variables:
        return f"{coef_str}{variables[0]} + {''.join(variables[1:])}" if len(variables) > 1 else f"{coef_str}{variables[0]}"
    else:
        return coef_str

def clave_ordenada(vars_con_exp):
    return tuple(sorted(vars_con_exp.items()))

def ingresar_expresion():
    n = int(input("¿Cuántos términos tendrá la expresión? "))
    expresion = defaultdict(float)

    for i in range(n):
        print(f"\nTérmino {i+1}:")
        coef = float(input("  Coeficiente: "))
        num_vars = int(input("  ¿Cuántas variables tiene este término? "))
        vars_con_exp = {}

        for j in range(num_vars):
            raw = input(f"    Variable #{j+1} (ej. x, y, z o varias: x,y): ").strip().lower()
            var_list = [v.strip() for v in raw.split(",")]
            exp = int(input(f"    Exponente de {raw}: "))
            for v in var_list:
                vars_con_exp[v] = vars_con_exp.get(v, 0) + exp

        clave = clave_ordenada(vars_con_exp)
        expresion[clave] += coef

    return expresion

def imprimir_expresion(expresion):
    partes = []
    for clave_vars, coef in expresion.items():
        vars_dict = dict(clave_vars)
        term = imprimir_termino_descompuesto(coef, vars_dict)
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
