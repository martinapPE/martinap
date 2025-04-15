def to_superindice(numero):
    superi = {"0":"⁰", "1":"¹", "2":"²", "3":"³", "4":"⁴", "5":"⁵",
              "6":"⁶", "7":"⁷", "8":"⁸", "9":"⁹", "-":"⁻"}
    return ''.join(superi[c] for c in str(numero))

def imprimir_polinomio(p):
    partes = []
    for exp in sorted(p.keys(), reverse=True):
        coef = p[exp]
        if coef == 0:
            continue

        coef_str = str(int(coef)) if coef.is_integer() else str(coef)

        if exp == 0:
            partes.append(f"{coef_str}")
        elif exp == 1:
            partes.append(f"{coef_str}x")
        else:
            partes.append(f"{coef_str}x{to_superindice(exp)}")
    return " + ".join(partes).replace("+ -", "- ")

def ingresar_monomio():
    coef = float(input("Ingrese el coeficiente del monomio: "))
    exp = int(input("Ingrese el exponente del monomio: "))
    return {exp: coef}

def ingresar_polinomio():
    n = int(input("¿Cuántos términos tendrá el polinomio? "))
    pol = {}
    for i in range(n):
        print(f"\nTérmino {i+1}:")
        coef = float(input("  Coeficiente: "))
        exp = int(input("  Exponente: "))
        if exp in pol:
            pol[exp] += coef
        else:
            pol[exp] = coef
    return pol

def main():
    print("=== REPRESENTADOR DE MONOMIOS Y POLINOMIOS ===")
    tipo = input("¿Deseas ingresar un monomio o un polinomio? (m/p): ").strip().lower()

    if tipo == 'm':
        pol = ingresar_monomio()
    elif tipo == 'p':
        pol = ingresar_polinomio()
    else:
        print("Opción no válida. Intenta de nuevo.")
        return

    print("\n🔹 Representación:")
    print(" ", imprimir_polinomio(pol))

if __name__ == "__main__":
    main()
