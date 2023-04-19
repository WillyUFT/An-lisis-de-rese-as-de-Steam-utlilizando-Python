## Instalamos los paquetes necesarios
import json
from typing import List, Dict


def mostrar_diccionario_como_json(diccionario: Dict):
    """
    Esta función hace que podamos ver un diccionario
    como un JSON, de esa forma es mucho mucho más legible

    Args:
        diccionario (dict): Por lo general serán las reviews
        que vienen en ese formato.
    """

    # Los ordenamos como JSON con una mejor indentación
    print(json.dumps(diccionario, indent=4))


def crear_compresion_de_diccionario_para_review(diccionario: Dict, autor: bool, columna: str, busqueda: str) -> Dict:
    """
    Esta función realiza una reducción de diccionario, esta consiste en tomar un diccionario
    y crear uno más pequeño basado en criterios de búsqueda, entonces, todas las entradas del diccionario
    que cumplan con dicho criterio serán insertados al diccionario reducido.

    Args:
        diccionario (dict): En este caso, será todo el diccionario que contiene todas las reviews.
        autor (bool): Es un booleano que nos indicará si los criterios de búsqueda tendrán que ser en las columnas dentro de la clave author
        o si buscamos fuera de ella. True para buscar dentro, false para buscar fuera.
        columna (str): Es el nombre de la columna en la que vamos a buscar la coindicencia. Puede ser cualquier string.
        busqueda (str): Es el criterio de búsqueda, aquella palabra o etiqueta que necesitamos buscar.

    Returns:
        dict: Diccionario reducido, el cual solo contiene entradas que cumplan con el string de búsqueda.
    """

    if autor:
        diccionario_reducido = {
            key: value
            for key, value in diccionario.items()
            if value["author"][columna] == busqueda
        }
        return diccionario_reducido
    else:
        diccionario_reducido = {
            key: value
            for key, value in diccionario.items()
            if value[columna] == busqueda
        }
        return diccionario_reducido
