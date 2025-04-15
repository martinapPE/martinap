# Paso 1: Pedir al usuario los milímetros
milimetros_input = float(input("Ingresa la cantidad en milímetros: "))

# Paso 2: Convertir a pulgadas
pulgadas = milimetros_input / 25.4

# Paso 3: Redondear a 2 decimales
pulgadas_redondeado = round(pulgadas, 2)

# Paso 4: Mostrar el resultado
print(f"{milimetros_input} mm equivalen a {pulgadas_redondeado} pulgadas.")
