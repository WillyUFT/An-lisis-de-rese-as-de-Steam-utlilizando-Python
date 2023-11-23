
# ! Este archivo es únicamente para comprobar el funcionamiento de la SteamReviewsAPI

## Importamos las librerías.
import steamreviews
import json

## Importamos los archivos.
from common.utilities import diccionarios
from common.utilities import tiempo
from common.config.steam import steamAPIConfiguration as steamConfig


# * Este es el juego de Hatsune Miku Logic Paint S: 2089350
miku = 2089350

# * Descargarmos las reviews que tiene
review_dict = steamreviews.download_reviews_for_app_id(
    miku)

print("\n\n\n")

print(review_dict);


reviews_miku = review_dict[0]["reviews"]

print(json.dumps(reviews_miku, indent=4))

# * Vamos ahora a mostrar únicamente la última reseña, para ver que tiene,
# * Para ello tenemos que primero transformar a lista y luego seleccionar cualquiera
# * Voy a sacar la entrada número 20, pero la verdad sirve cualquiera.
reviews_miku_list = list(review_dict[0]["reviews"].values())
print(len(reviews_miku_list))
review_aleatoria = reviews_miku_list[200]
diccionarios.mostrar_diccionario_como_json(review_aleatoria)

# * Voy a buscar por mi steam id
review_willy = diccionarios.crear_compresion_de_diccionario_para_review(
    reviews_miku, True, "steamid", steamConfig.STEAM_ID
)

print("\n\n\n")

# * Vamos a buscar los valores de los tiempos jugados y la review
for reviewId, sub_dict in review_willy.items():
    review = sub_dict.get('review', '')
    playtime_forever = sub_dict['author'].get('playtime_forever', 0)
    playtime_at_review = sub_dict['author'].get('playtime_at_review', 0)
    
    print(f"Review: {review}")
    print(f"Play time forever: {tiempo.minutos_a_hhmm(playtime_forever)}")
    print(f"Play time at review: {tiempo.minutos_a_hhmm(playtime_at_review)}")