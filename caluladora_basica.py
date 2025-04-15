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

    # Procedimiento resaltado en comillas y 'negrita' (mayúsculas)
    print(Fore.MAGENTA + '\n"SELECCIONA LA OPERACIÓN RESPECTIVA, PRESIONANDO LA TECLA CORRESPONDIENTE EN EL TECLADO Y PRESIONA ENTER."\n')

def pedir_valores():
    try:
        a = float(input(Fore.GREEN + "\nIngresa el primer número: "))
        b = float(input(Fore.GREEN + "Ingresa el segundo número: "))
        return a, b
    except ValueError:
        print(Fore.RED + "\n⚠️  Error: Ingresa solo números válidos.\n")
        return None, None

def realizar_operacion(op, a, b):
    if op == "+":
        resultado = a + b
        print(Fore.CYAN + f"\nResultado: {a} + {b} = {resultado}")
    elif op == "-":
        resultado = a - b
        print(Fore.CYAN + f"\nResultado: {a} - {b} = {resultado}")
    elif op == "*":
        resultado = a * b
        print(Fore.CYAN + f"\nResultado: {a} * {b} = {resultado}")
    elif op == "/":
        if b == 0:
            print(Fore.RED + "\n⚠️  Error: No se puede dividir entre cero.")
        else:
            resultado = a / b
            print(Fore.CYAN + f"\nResultado: {a} / {b} = {resultado}")

def main():
    while True:
        mostrar_menu()
        operacion = input(Fore.CYAN + Style.BRIGHT + "\nSelecciona una operación (+, -, *, /, x para salir): ").strip()

        if operacion.lower() == "x":
            print(Fore.CYAN + "\nGracias por usar la calculadora. ¡Hasta pronto! 👋\n")
            break
        elif operacion in ["+", "-", "*", "/"]:
            a, b = pedir_valores()
            if a is not None and b is not None:
                realizar_operacion(operacion, a, b)
        else:
            print(Fore.RED + "\n⚠️  Opción inválida. Por favor elige una operación válida.\n")

if __name__ == "__main__":
    main()

