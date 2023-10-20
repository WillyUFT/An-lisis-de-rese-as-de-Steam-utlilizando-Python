# ! Este archivo recogerá las reviews de Steam de juegos Metroidvania

# ^^ Para esta sección se utilizan los datos de SteamSpy,
# ^^ el autor autoriza el uso de su API para esta tesis.

# ? Importamos los librerías.
import requests
import itertools
import pandas
import steamreviews

# ? Importamos las funciones propias del programa
from common.utilities import tiempo

########## ! PRIMERO LO HAREMOS CON HOLOLIVE ! ##########

# * Antes de comenzar todo esto, voy a generar unos los juegos de hololive en Steam.
data_hololive = [
    {'app_id':'2062550', 'app_name':'hololive ERROR'},
    {'app_id':'1742020', 'app_name':'Idol Showdown'},
    {'app_id':'1748610', 'app_name':'Evil God Korone'}
]

juegos_hololive = pandas.DataFrame(data_hololive)

# & Primero creamos una lista vacía en la que irán todos los data frames de las reseñas
reseñas_hololive = [] # Reseñas para hololive
reseñas_metroidvania = [] # Reseñas para juegos metroidvania

# * Acá obtenemos recorremos el data frame y buscamos las reseñas de hololive
for index, row in juegos_hololive.iterrows():
    # ? Buscamos las reseñas del juego que se está iterando ahora mismo
    review_dict = steamreviews.download_reviews_for_app_id(int(row["app_id"]))

    # * Lamentablemente, para ir añadiendo reseñas a la lista tenemos que hacer un for dentro de otro, perdóname Hidalgo
    for review_id in review_dict[0]["reviews"]:
        
        # * Sacaremos los datos relevantes
        app_id = row["app_id"] # ID del juego
        app_name = row["app_name"] # Nombre del juego
        
        review_data = review_dict[0]["reviews"][review_id] # Acá está toda la info de la review
        
        review = review_data["review"]
        playtime = tiempo.minutos_a_hhmm(review_data["author"]["playtime_forever"])
        
         # Agregar el diccionario a la lista
        reseñas_hololive.append({
            'app_id': app_id, 
            'app_name': app_name, 
            'review': review,
            'playtime': playtime,
        })

# * Creamos el dataframe de reseñas
reseñas_df = pandas.DataFrame(reseñas_hololive)

# * Guardar el DataFrame como un archivo de Excel, esto porque el programa se demora demasiado, necesitamos los datos más a la mano
reseñas_df.to_excel("reviews hololive.xlsx", index=False)

########## ! AHORA CON VIDEOJUEGOS METROIDVANIA ! ##########


# * Creamos la url que sirve para ir a buscar los juegos por tags,
# * El parámetro puede ser cambiado por otro, pero para este caso se
# * necesita "Metroidvania".
url = "http://www.steamspy.com/api.php?request=tag&tag=Metroidvania"

# * Acá se trae la data.
response = requests.get(url)
data = response.json()

# ? La respuesta trae demasiados juegos, no es necesario tener todos
# ? por lo que se limitará la lista de juegos a solo 500.
data = dict(itertools.islice(data.items(), 500))

# * Creamos una lista vacía para que almacene unos diccionarios separados.
juegos = []

# & Se llenan las listas con los nombres y los id de los juegos.
for app_id, app_info in data.items():
    juego = {"app_id": app_id, "app_name": app_info["name"]}
    juegos.append(juego)

# * Creamos un dataframe con los juegos que analizaremos
juegos_df = pandas.DataFrame(juegos)

reseñas_metroidvania = [] # Reseñas para juegos metroidvania

# * Acá obtenemos recorremos el data frame y buscamos las reseñas de hololive
for index, row in juegos_df.iterrows():
    # ? Buscamos las reseñas del juego que se está iterando ahora mismo
    review_dict = steamreviews.download_reviews_for_app_id(int(row["app_id"]))

    # * Lamentablemente, para ir añadiendo reseñas a la lista tenemos que hacer un for dentro de otro, perdóname Hidalgo
    for review_id in review_dict[0]["reviews"]:
        
        # * Sacaremos los datos relevantes
        app_id = row["app_id"] # ID del juego
        app_name = row["app_name"] # Nombre del juego
        
        review_data = review_dict[0]["reviews"][review_id] # Acá está toda la info de la review
        
        review = review_data["review"]
        playtime_forever = tiempo.minutos_a_hhmm(review_data["author"]["playtime_forever"])
        
         # Agregar el diccionario a la lista
        reseñas_metroidvania.append({
            'app_id': app_id, 
            'app_name': app_name, 
            'review': review,
            'playtime_forever': playtime_forever,
        })

# * Creamos el dataframe de reseñas
reseñas_df = pandas.DataFrame(reseñas_metroidvania)

# * Guardar el DataFrame como un archivo de Excel, esto porque el programa se demora demasiado, necesitamos los datos más a la mano
reseñas_df.to_excel("reviews metroidvania.xlsx", index=False)