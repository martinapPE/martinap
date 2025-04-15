from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

def mostrar_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n=== CALCULADORA BÁSICA ===")
    print(Fore.YELLOW + "Operaciones disponibles:")
    print(Fore.YELLOW + "  +  → Suma")
    print(Fore.YELLOW + "  -  → Resta")
    print(Fore.YELLOW + "  *  → Multiplicación")
    print(Fore.YELLOW + "  /  → División")
    print(Fore.YELLOW + "  x  → Salir del programa")
    print(Fore.MAGENTA + '\n"SELECCIONA LA OPERACIÓN RESPECTIVA, PRESIONANDO LA TECLA CORRESPONDIENTE EN EL TECLADO Y PRESIONA ENTER."\n')

def pedir_valores():
    print(Fore.LIGHTMAGENTA_EX + "Puedes ingresar números enteros o decimales (usa punto '.' para los decimales).\n")
    try:
        a = float(input(Fore.GREEN + "Ingresa el primer número: "))
        b = float(input(Fore.GREEN + "Ingresa el segundo número: "))
        return a, b
    except ValueError:
        print(Fore.RED + "\n⚠️  Error: Ingresa solo números válidos.\n")
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
        else:
            return a / b

def comparar_resultados(res1, res2):
    if res1 > res2:
        print(Fore.CYAN + f"\n🔎 El resultado de la primera operación ({res1}) es mayor que el de la segunda operación ({res2}).")
    elif res1 < res2:
        print(Fore.CYAN + f"\n🔎 El resultado de la segunda operación ({res2}) es mayor que el de la primera operación ({res1}).")
    else:
        print(Fore.CYAN + f"\n🔎 Ambos resultados son iguales: {res1} = {res2}")

def main():
    while True:
        mostrar_menu()

        # Elegir dos operaciones
        operacion1 = input(Fore.CYAN + Style.BRIGHT + "\nSelecciona la primera operación (+, -, *, /, x para salir): ").strip()
        if operacion1.lower() == "x":
            print(Fore.CYAN + "\nGracias por usar la calculadora. ¡Hasta pronto! 👋\n")
            break
        elif operacion1 not in ["+", "-", "*", "/"]:
            print(Fore.RED + "\n⚠️  Opción inválida para la primera operación.\n")
            continue

        operacion2 = input(Fore.CYAN + Style.BRIGHT + "\nSelecciona la segunda operación (+, -, *, /, x para salir): ").strip()
        if operacion2.lower() == "x":
            print(Fore.CYAN + "\nGracias por usar la calculadora. ¡Hasta pronto! 👋\n")
            break
        elif operacion2 not in ["+", "-", "*", "/"]:
            print(Fore.RED + "\n⚠️  Opción inválida para la segunda operación.\n")
            continue

        # Pedir valores para ambas operaciones
        print(Fore.CYAN + "\n--- Primer operación ---")
        a1, b1 = pedir_valores()
        if a1 is None or b1 is None:
            continue

        print(Fore.CYAN + "\n--- Segunda operación ---")
        a2, b2 = pedir_valores()
        if a2 is None or b2 is None:
            continue

        # Realizar operaciones
        res1 = realizar_operacion(operacion1, a1, b1)
        res2 = realizar_operacion(operacion2, a2, b2)

        # Mostrar resultados en celeste y comparar
        if res1 is not None and res2 is not None:
            res1 = round(res1, 3)
            res2 = round(res2, 3)

            print(Fore.CYAN + f"\nResultado 1: {a1} {operacion1} {b1} = {res1}")
            print(Fore.CYAN + f"Resultado 2: {a2} {operacion2} {b2} = {res2}")
            comparar_resultados(res1, res2)

if __name__ == "__main__":
    main()
