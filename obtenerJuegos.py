
# * ---------------------------------------------------------------------------- * #
# *                         ¿PARA QUÉ SIRVE ESTE ARCHIVO?                        * #
# * ---------------------------------------------------------------------------- * #

# Este archivo py va a buscar a steamspy los juegos que pertenecen a cierto tag.
# Luego los guardaremos en un json, porque a veces la api se cae, así que para no
# depender de ella guardaremos la selección.

# * ---------------------------------------------------------------------------- * #
# *                                 IMPORTACIONES                                * #
# * ---------------------------------------------------------------------------- * #
import requests
import json
import os

# * ---------------------------------------------------------------------------- * #
# *                                   VARIABLES                                  * #
# * ---------------------------------------------------------------------------- * #
juegosABuscar: list = [
    "metroidvania",
    "indie",
    "anime",
    "action",
    "2D",
    "female+protagonist",
]

buscar: bool = True

# * ---------------------------------------------------------------------------- * #
# *                                    CÓDIGO                                    * #
# * ---------------------------------------------------------------------------- * #


# * Buscamos los juegos que exsten
def buscar_juegos():
    if buscar:
        for i in range(0, len(juegosABuscar) - 1):
            # & Obtenemos la lista completa de juegos de Steam
            url = f"https://steamspy.com/api.php?request=tag&tag={juegosABuscar[i]}"

            response = requests.get(url)
            data = response.json()

            comprobar_carpeta_data()

            # & Guardamos los juegos en Json enorme
            with open(f"data/listajuegos/juegos_{juegosABuscar[i]}.json", "w") as file:
                json.dump(data, file)
    else:
        print("No vamos a buscar juegos por ahora, para buscar cambia 'buscar' a true")


# * Comprobar si la carpeta 'data/listajuegos' existe, si no, crearla
def comprobar_carpeta_data() -> None:
    if not os.path.exists("data/listajuegos"):
        os.makedirs("data/listajuegos")


buscar_juegos()
