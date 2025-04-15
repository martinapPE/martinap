from fractions import Fraction

# Crear dos fracciones
a = Fraction(3, 4)   # 3/4
b = Fraction(5, 6)   # 5/6

# Suma
suma = a + b

# Resta
resta = a - b

# Multiplicación
multiplicacion = a * b

# División
division = a / b

# Mostrar resultados
print(f"Suma: {a} + {b} = {suma}")
print(f"Resta: {a} - {b} = {resta}")
print(f"Multiplicación: {a} * {b} = {multiplicacion}")
print(f"División: {a} / {b} = {division}")
from fractions import Fraction

# Definir el número como fracción
decimal = 11.23

# Convertir el número decimal a una fracción
fraccion = Fraction(decimal).limit_denominator()  # Para simplificar la fracción automáticamente

# Mostrar el resultado
print(f"{decimal} en fracción es: {fraccion}")

# ========================
# Conversión pulgadas a milímetros
# ========================
# Conversión de pulgadas a milímetros con redondeo a 2 decimales

# Paso 1: Definir el valor en pulgadas
pulgadas = 5.32  # Puedes cambiar este valor por el que quieras

# Paso 2: Realizar la conversión
milimetros = pulgadas * 25.4

# Paso 3: Redondear a 2 decimales
milimetros_redondeado = round(milimetros, 2)

# Paso 4: Mostrar el resultado
print(f"{pulgadas} pulgadas son {milimetros_redondeado} milímetros.")
