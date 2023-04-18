## Importamos las librerías.
import steamreviews
import json

#* Este es el juego de Miku: 2089350
miku = 2089350

#! Lista final
reviews = []

# Configura la API de Steam
request_params = {
    'filter': 'recent',  # Ordena las reseñas por fecha
    'language': 'all',   # Obtiene reseñas en todos los idiomas
    'day_range': '30',   # Obtiene reseñas de los últimos 30 días
    'num_per_page': 5, # Obtiene 100 reseñas por solicitud
}

#* Descargarmos las reviews que tiene
review_dict = steamreviews.download_reviews_for_app_id(miku, chosen_request_params=request_params)
reviews_miku = review_dict[0]['reviews']

# Iterar a través de las claves y valores del diccionario
for value in reviews_miku.values():
    playtime_forever = value['author']['playtime_forever']
    review = value['review']
    
    print(f"Playtime forever: {playtime_forever}")
    print(f"Review: {review}\n")

