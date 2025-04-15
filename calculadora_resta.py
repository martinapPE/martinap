from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

def main():
    print(Fore.CYAN + Style.BRIGHT + "\n=== Calculadora de Resta con Suma Previa ===\n")

    try:
        # Solicita los valores
        a = int(input(Fore.YELLOW + "Ingresa el primer número (ej. -12): "))
        b = int(input(Fore.YELLOW + "Ingresa el segundo número que se suma al primero (ej. 9): "))
        h = int(input(Fore.YELLOW + "Ingresa el número que se restará al resultado (ej. 7): "))

        g = a + b

        # Muestra los resultados con formato
        print(Fore.GREEN + f"\nOperación: ({a}) + ({b}) = {g}")
        print(Fore.MAGENTA + f"Resta final: {g} - {h} = {g - h}\n")

    except ValueError:
        print(Fore.RED + "\nError: Por favor ingresa solo números enteros.\n")

if __name__ == "__main__":
    main()
