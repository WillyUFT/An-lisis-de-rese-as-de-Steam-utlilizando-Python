
# ! Este archivo recogerá las reviews de Steam de juegos de Hololive, que son poquitos

# ^^ Para esta sección se utilizan los datos de SteamSpy,
# ^^ el autor autoriza el uso de su API para esta tesis.

# ? Importamos los librerías.
import pandas
import steamreviews

# ? Importamos las funciones propias del programa
from common.utilities import tiempo

########## ! PRIMERO LO HAREMOS CON HOLOLIVE ! ##########

# * Antes de comenzar todo esto, voy a generar unos los juegos de hololive en Steam.
data_hololive = [
    {'app_id':'2062550', 'app_name':'hololive ERROR'},
    {'app_id':'1742020', 'app_name':'Idol Showdown'},
    {'app_id':'1748610', 'app_name':'Evil God Korone'},
    {'app_id':'2420510', 'app_name': 'HoloCure - Save the Fans!'},
    {'app_id':'2494480', 'app_name':'Truth of Beauty Witch -Marine\'s treasure ship-'}
]

request_params = {"language": "english,spanish", "num_per_page": "100"}  # Máximo es 100
limite_de_resenas = 100000


juegos_hololive = pandas.DataFrame(data_hololive)

# & Primero creamos una lista vacía en la que irán todos los data frames de las reseñas
reseñas_hololive = [] # Reseñas para hololive

# * Acá obtenemos recorremos el data frame y buscamos las reseñas de hololive
for index, row in juegos_hololive.iterrows():
    # ? Buscamos las reseñas del juego que se está iterando ahora mismo
    review_dict = steamreviews.download_reviews_for_app_id(
            int(row["app_id"]),
            chosen_request_params=request_params,
            limite_resenas=limite_de_resenas,
        )

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
reseñas_df.to_excel("juegos_hololive.xlsx", index=False)

