"""
    Reloj que se actualiza en consola cada seg
"""
import time
from datetime import datetime

while True:
    # Almacena el dato tiempo actual con un formato definido en la variable
    # strftime significa string format time
    hora_actual = datetime.now().strftime("%H : %M : %S")
    print(f"\rHora actual {hora_actual}", end="")
    # Actualiza la impresion de infor en consola cada segundo,
    time.sleep(1)

