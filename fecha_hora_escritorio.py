from datetime import datetime
import time
import locale
import tkinter as tk

# Establecer la configuración regional a español
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')  # Prueba con 'es_ES.utf8' o 'Spanish_Spain.1252' si 'es_ES' no funciona

# Crear la ventana principal
root = tk.Tk()
root.title("Fecha y Hora Actual")

# Crear una etiqueta para mostrar la fecha y hora
label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

def actualizar_reloj():
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()
    
    # Determinar AM o PM
    am_pm = "AM" if fecha_hora_actual.hour < 12 else "PM"
    
    # Formatear la fecha y hora actual en formato de 12 horas con día de la semana en español
    fecha_hora_formateada = fecha_hora_actual.strftime(f"%A, %Y-%m-%d %I:%M:%S {am_pm}")
    
    # Actualizar la etiqueta con la fecha y hora formateada
    label.config(text=f"Fecha y hora actual: {fecha_hora_formateada}")
    
    # Llamar a esta función nuevamente después de 1000 milisegundos (1 segundo)
    label.after(1000, actualizar_reloj)

# Iniciar la actualización del reloj
actualizar_reloj()

# Ejecutar la aplicación
root.mainloop()

