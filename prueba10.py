from fractions import Fraction

# Crear fracciones
f1 = Fraction(3, 4)
f2 = Fraction(2, 5)

# Operaciones básicas
suma = f1 + f2
resta = f1 - f2
producto = f1 * f2
division = f1 / f2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {producto}")
print(f"División: {division}")
f3 = Fraction(0.75)  # Automáticamente lo convierte a 3/4
print(f3)
f4 = Fraction(10, 20)  # Devuelve 1/2
print(f4)
