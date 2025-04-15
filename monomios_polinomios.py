def imprimir_polinomio(p):
    partes = []
    for exp in sorted(p.keys(), reverse=True):
        coef = p[exp]
        if coef == 0:
            continue
        if exp == 0:
            partes.append(f"{coef}")
        elif exp == 1:
            partes.append(f"{coef}x")
        else:
            partes.append(f"{coef}x^{exp}")
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
            pol[exp] += coef  # suma si ya existe el mismo exponente
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

