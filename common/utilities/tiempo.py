## Importamos los paquetes
from datetime import datetime


def minutos_a_hhmm(minutos: int) -> str:
    
    """
    Esta función toma un número de minutos y los transforma a horas y minutos.

    Args:
        minutos (int): Cantidad de minutos, en formato numérico.

    Returns:
        str: Entrega la misma cantidad de minutos, pero representado en horas y minutos, EJ: 15:40
    """

    horas, minutos = divmod(minutos, 60)
    return f"{horas:02d}:{minutos:02d}"


def formatear_fecha(fecha: datetime) -> str:
    
    """
    Esta función toma una fecha en formato YYYY-MM-DD HH:mm:ss
    y lo transforma a DD-MM-YYYY HH:mm

    Returns:
        str: Fecha en formato DD-MM-YYYY HH:mm
    """
    
    # Formateamos el objeto datetime en el formato deseado
    fecha_formateada = fecha.strftime("%d-%m-%Y %H:%M")
    
    return fecha_formateada
