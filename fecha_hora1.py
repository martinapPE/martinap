from datetime import datetime
import time

while True:
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()
    
    # Formatear la fecha y hora actual en formato de 12 horas
    fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %I:%M:%S %p")
    
    # Imprimir la fecha y hora actual
    print(f"Fecha y hora actual: {fecha_hora_formateada}", end='\r')
    
    # Esperar un segundo antes de actualizar
    time.sleep(1)
    
    from datetime import datetime
import time

while True:
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()
    
    # Formatear la fecha y hora actual en formato de 12 horas con día de la semana
    fecha_hora_formateada = fecha_hora_actual.strftime("%A, %Y-%m-%d %I:%M:%S %p")
    
    # Imprimir la fecha y hora actual
    print(f"Fecha y hora actual: {fecha_hora_formateada}", end='\r')
    
    # Esperar un segundo antes de actualizar
    time.sleep(1)
    
    
    
    