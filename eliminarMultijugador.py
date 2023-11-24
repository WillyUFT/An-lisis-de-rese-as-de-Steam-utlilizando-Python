
# ! Este archivo elimina de los json todos los juegos multijugador

# * ========================================================================= #
# *                              IMPORTACIONES                               #
# * ========================================================================= #
import json



# * ========================================================================= #
# *                                 VARIABLES                                 #
# * ========================================================================= #
listaJuegos = [
    "juegos_anime",
    "juegos_indie",
    "juegos_metroidvania",
    "juegos_female+protagonist"
]

# ~ ========================================================================= #
# ~              SACAMOS EL FACTOR MULTIJUGADOR CASI POR COMPLETO             #
# ~ ========================================================================= #

# * Cargamos el json de juegos multijugador
with open('data/listaJuegos/juegos_multijugador.json', 'r') as file:
    juegos_multijugador = json.load(file)

# * Convertimos el diccionario de juegos multijugador a un conjunto de appids
multijugador_appids = {int(appid) for appid in juegos_multijugador.keys()}

# * recorremos la lista de los juegos
for categoria in listaJuegos:
    with open(f'data/listaJuegos/{categoria}.json', 'r') as file:
        juegos_categoria = json.load(file)
        
    # * Filtrar juegos que no son multijugador
    juegos_filtrados = {appid: info for appid, info in juegos_categoria.items() if int(appid) not in multijugador_appids}

    # * Guardar los juegos filtrados de vuelta al archivo JSON
    with open(f'data/listaJuegos/{categoria}.json', 'w') as file:
        json.dump(juegos_filtrados, file, indent=4)

# ~ ========================================================================= #
# ~                 AHORA LIMITAMOS EL JSON A SOLO 200 JUEGOS                 #
# ~ ========================================================================= #

# * recorremos la lista de los juegos
for categoria in listaJuegos:
    with open(f'data/listaJuegos/{categoria}.json', 'r') as file:
        juegos_categoria = json.load(file)

    # * Limitar a las primeras 50 entradas
    primeras_200_entradas = dict(list(juegos_categoria.items())[:50])

    # Guardar las primeras 200 entradas de vuelta al archivo JSON
    with open(f'data/listaJuegos/{categoria}.json', 'w') as file:
        json.dump(primeras_200_entradas, file, indent=4)