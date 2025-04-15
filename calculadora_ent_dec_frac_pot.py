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
    print(Fore.LIGHTWHITE_EX + "- Evita dejar espacios entre el número y el símbolo '/' en las fracciones.")
    print(Fore.LIGHTWHITE_EX + "- El programa reconocerá automáticamente el tipo de número e interpretará correctamente la operación.\n")

def pedir_valores():
    print(Fore.LIGHTMAGENTA_EX + "Puedes ingresar números enteros, decimales o fracciones (ej: 3, 4.5, 2/3).")
    try:
        a = Fraction(input(Fore.GREEN + "Ingresa el primer número: "))
        b = Fraction(input(Fore.GREEN + "Ingresa el segundo número: "))
        return a, b
    except (ValueError, ZeroDivisionError):
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
    elif op == "^":  # Para la operación de exponentes
        return a ** b

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
        mostrar_reseña_entrada()  # ← Aquí se llama la reseña

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
            # Mostramos los resultados como fracción y también el decimal como referencia
            dec1 = round(float(res1), 3)
            dec2 = round(float(res2), 3)

            print(Fore.CYAN + f"\nResultado 1: {a1} {operacion1} {b1} = " +
                  Fore.LIGHTCYAN_EX + f"{res1} (fracción)  " +
                  Fore.LIGHTBLACK_EX + f"≈ {dec1} (decimal)")
            print(Fore.CYAN + f"Resultado 2: {a2} {operacion2} {b2} = " +
                  Fore.LIGHTCYAN_EX + f"{res2} (fracción)  " +
                  Fore.LIGHTBLACK_EX + f"≈ {dec2} (decimal)")

            comparar_resultados(res1, res2)

if __name__ == "__main__":
    main()
