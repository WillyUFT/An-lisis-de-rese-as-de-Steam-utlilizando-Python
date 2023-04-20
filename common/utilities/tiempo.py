def minutos_a_hhmm(minutos):
    """
    Esta función toma un número de minutos y los transforma a horas y minutos.

    Args:
        minutos (int): Cantidad de minutos, en formato numérico.

    Returns:
        string: Entrega la misma cantidad de minutos, pero representado en horas y minutos, EJ: 15:40
    """

    horas, minutos = divmod(minutos, 60)
    return f"{horas:02d}:{minutos:02d}"
