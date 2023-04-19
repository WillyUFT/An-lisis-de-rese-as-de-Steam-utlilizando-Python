## Importamos las librerías.
import steamreviews

## Importamos los archivos.
from common.utilities import diccionarios
from common.config import steamReviewsAPIConfiguration as steamReviewsConfig
from common.config import steamAPIConfiguration as steamConfig

# * Este es el juego de Hatsune Miku Logic Paint S: 2089350
miku = 2089350

#! Lista final
reviews = []

# * Descargarmos las reviews que tiene
review_dict = steamreviews.download_reviews_for_app_id(
    miku, chosen_request_params=steamReviewsConfig.filtros
)
reviews_miku = review_dict[0]["reviews"]

# * Vamos ahora a mostrar únicamente la última reseña, para ver que tiene,
# * Para ello tenemos que primero transformar a lista y luego seleccionar cualquiera
# * Voy a sacar la entrada número 39, pero la verdad sirve cualquiera.
reviews_miku_list = list(review_dict[0]["reviews"].values())
review_aleatoria = reviews_miku_list[200]
diccionarios.mostrar_diccionario_como_json(review_aleatoria)

# * Voy a buscar por mi steam id
review_willy = diccionarios.crear_compresion_de_diccionario_para_review(
    reviews_miku, True, "steamid", steamConfig.STEAM_ID
)

# * Vamos a ver si existe el comentario que hice antes
review = review_willy["review"]
steam_id = review_willy["author"]["steamid"]

print(f"Steam ID: {steam_id}")
print(f"Review: {review}\n")
