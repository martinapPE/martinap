from fractions import Fraction

# Paso 1: Pedir al usuario los milímetros
milimetros_input = float(input("Ingresa la cantidad en milímetros: "))

# Paso 2: Convertir a pulgadas en decimal
pulgadas_decimal = milimetros_input / 25.4

# Paso 3: Convertir el valor decimal a fracción
pulgadas_fraccion = Fraction(pulgadas_decimal).limit_denominator()  # Convierte a fracción

# Paso 4: Redondear la parte decimal a 2 decimales
pulgadas_decimal_redondeado = round(pulgadas_decimal, 2)

# Paso 5: Mostrar el resultado en formato decimal y fracción
print(f"{milimetros_input} mm equivalen a {pulgadas_decimal_redondeado} pulgadas (en decimal) o {pulgadas_fraccion} pulgadas (en fracción).")
