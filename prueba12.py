from fractions import Fraction
import math

# Denominador fijo para fracciones comerciales (1/32")
DENOMINADOR = 32

try:
    mm = float(input("Ingresa la medida en milímetros: "))
    pulgadas = mm / 25.4
    entero = int(pulgadas)
    decimal = pulgadas - entero

    # Convertimos la parte decimal a 1/32 y redondeamos hacia arriba
    fr = Fraction(decimal).limit_denominator(DENOMINADOR)

    if float(fr) < decimal:
        num = math.ceil(fr.numerator * DENOMINADOR / fr.denominator)
        fr = Fraction(num, DENOMINADOR)

    if fr.numerator >= fr.denominator:
        entero += 1
        fr = Fraction(0)

    print(f"\nResultado:")
    print(f"- Decimal: {round(pulgadas, 3)}\"")
    if fr != 0:
        print(f"- Fracción comercial: {entero} {fr}\" (en 1/32)")
    else:
        print(f"- Fracción exacta: {entero}\"")

except ValueError:
    print("Entrada no válida. Usa solo números.")
