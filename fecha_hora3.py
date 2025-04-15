from datetime import datetime
import time
import locale

# Establecer la configuración regional a español
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')  # Prueba con 'es_ES.utf8' o 'Spanish_Spain.1252' si 'es_ES' no funciona

while True:
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()
    
    # Determinar AM o PM
    am_pm = "AM" if fecha_hora_actual.hour < 12 else "PM"
    
    # Formatear la fecha y hora actual en formato de 12 horas con día de la semana en español
    fecha_hora_formateada = fecha_hora_actual.strftime(f"%A, %Y-%m-%d %I:%M:%S {am_pm}")
    
    # Imprimir la fecha y hora actual
    print(f"Fecha y hora actual: {fecha_hora_formateada}", end='\r')
    
    # Esperar un segundo antes de actualizar
    time.sleep(1)
    
    
    
    
    
    