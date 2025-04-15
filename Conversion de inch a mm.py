from fractions import Fraction

# Paso 1: Pedir al usuario la fracción
fraccion_input = input("Ingresa una fracción (por ejemplo 5/32): ")

# Paso 2: Convertir la fracción a un tipo Fraction
fraccion_pulgada = Fraction(fraccion_input)  # Convierte la entrada en una fracción

# Paso 3: Convertir a milímetros
milimetros = float(fraccion_pulgada) * 25.4

# Paso 4: Redondear a 2 decimales
milimetros_redondeado = round(milimetros, 2)

# Paso 5: Mostrar el resultado
print(f"{fraccion_pulgada} pulgadas equivalen a {milimetros_redondeado} mm.")
