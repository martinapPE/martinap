from colorama import init, Fore, Style
from fractions import Fraction

init(autoreset=True)

def mostrar_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n=== CALCULADORA DE FRACCIONES Y DECIMALES ===")
    print(Fore.YELLOW + "Operaciones disponibles:")
    print(Fore.YELLOW + "  +  → Suma")
    print(Fore.YELLOW + "  -  → Resta")
    print(Fore.YELLOW + "  *  → Multiplicación")
    print(Fore.YELLOW + "  /  → División")
    print(Fore.YELLOW + "  ^  → Exponentes (Potencia)")
    print(Fore.YELLOW + "  x  → Salir del programa")
    print(Fore.MAGENTA + '\n"SELECCIONA LA OPERACIÓN RESPECTIVA, PRESIONANDO LA TECLA CORRESPONDIENTE EN EL TECLADO Y PRESIONA ENTER."\n')

def mostrar_reseña_entrada():
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + "\n📌 Instrucciones para ingresar números:")
    print(Fore.LIGHTWHITE_EX + "- Puedes escribir números de las siguientes formas:")
    print(Fore.LIGHTGREEN_EX + "    ✔ Entero      → 4, -2")
    print(Fore.LIGHTGREEN_EX + "    ✔ Decimal     → 3.5, -0.75")
    print(Fore.LIGHTGREEN_EX + "    ✔ Fracción    → 2/3, -5/7, 7/1")
    print(Fore.LIGHTGREEN_EX + "    ✔ Exponentes  → Para ingresar un exponente usa el símbolo '^'. Ejemplo: 2^3 para 2 elevado a 3.")
    print(Fore.LIGHTWHITE_EX + "- Evita dejar espacios entre el número y el símbolo '/' en las fracciones.")
    print(Fore.LIGHTWHITE_EX + "- El programa reconocerá automáticamente el tipo de número e interpretará correctamente la operación.\n")

def evaluar_entrada(cadena):
    try:
        if "^" in cadena:
            base, exp = cadena.split("^")
            base_eval = evaluar_entrada(base.strip())
            exp_eval = evaluar_entrada(exp.strip())
            return base_eval ** exp_eval
        return Fraction(cadena)
    except:
        raise ValueError("Entrada inválida")

def pedir_valores():
    print(Fore.LIGHTMAGENTA_EX + "Puedes ingresar números enteros, decimales, fracciones o exponentes (ej: 3, 4.5, 2/3, 2^3).")
    try:
        a = evaluar_entrada(input(Fore.GREEN + "Ingresa el primer número: "))
        b = evaluar_entrada(input(Fore.GREEN + "Ingresa el segundo número: "))
        return a, b
    except:
        print(Fore.RED + "\n⚠️  Error: Asegúrate de ingresar valores válidos.")
        return None, None

def realizar_operacion(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            print(Fore.RED + "\n⚠️  Error: No se puede dividir entre cero.")
            return None
        return a / b
    elif op == "^":
        try:
            return a ** b
        except:
            print(Fore.RED + "\n⚠️  Error: Potencia inválida.")
            return None

def mostrar_resultado(res, etiqueta):
    dec = float(res)
    if abs(dec) > 1e6 or abs(dec) < 1e-4:
        print(Fore.CYAN + f"{etiqueta} = " + Fore.LIGHTCYAN_EX + f"≈ {dec:.6e} (decimal)")
    else:
        print(Fore.CYAN + f"{etiqueta} = " + Fore.LIGHTCYAN_EX + f"{res} (fracción)  ≈ {round(dec, 6)}")

def comparar_resultados(res1, res2):
    if res1 > res2:
        print(Fore.CYAN + f"\n🔎 El resultado 1 ({res1}) es mayor que el resultado 2 ({res2}).")
    elif res1 < res2:
        print(Fore.CYAN + f"\n🔎 El resultado 2 ({res2}) es mayor que el resultado 1 ({res1}).")
    else:
        print(Fore.CYAN + f"\n🔎 Ambos resultados son iguales: {res1} = {res2}")

def main():
    while True:
        mostrar_menu()
        mostrar_reseña_entrada()

        operacion1 = input(Fore.CYAN + Style.BRIGHT + "\nSelecciona la primera operación (+, -, *, /, ^, x para salir): ").strip()
        if operacion1.lower() == "x":
            print(Fore.CYAN + "\nGracias por usar la calculadora. ¡Hasta pronto! 👋\n")
            break
        elif operacion1 not in ["+", "-", "*", "/", "^"]:
            print(Fore.RED + "\n⚠️  Opción inválida para la primera operación.")
            continue

        operacion2 = input(Fore.CYAN + Style.BRIGHT + "\nSelecciona la segunda operación (+, -, *, /, ^, x para salir): ").strip()
        if operacion2.lower() == "x":
            print(Fore.CYAN + "\nGracias por usar la calculadora. ¡Hasta pronto! 👋\n")
            break
        elif operacion2 not in ["+", "-", "*", "/", "^"]:
            print(Fore.RED + "\n⚠️  Opción inválida para la segunda operación.")
            continue

        print(Fore.CYAN + "\n--- Primera operación ---")
        a1, b1 = pedir_valores()
        if a1 is None or b1 is None:
            continue

        print(Fore.CYAN + "\n--- Segunda operación ---")
        a2, b2 = pedir_valores()
        if a2 is None or b2 is None:
            continue

        res1 = realizar_operacion(operacion1, a1, b1)
        res2 = realizar_operacion(operacion2, a2, b2)

        if res1 is not None and res2 is not None:
            print()
            mostrar_resultado(res1, f"Resultado 1: {a1} {operacion1} {b1}")
            mostrar_resultado(res2, f"Resultado 2: {a2} {operacion2} {b2}")

            comparar_resultados(float(res1), float(res2))

if __name__ == "__main__":
    main()
