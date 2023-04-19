#!!!!!!!!!!!!!!!!!!!!!!!! Acá únicamente vamos a dejar las variables de Steam API !!!!!!!!!!!!!!!!!!!!!

#* Configuramos los parámetros de búsqueda de reseñas.
filtros = {
    'filter': 'recent',  # Ordena las reseñas por fecha
    'language': 'all',   # Obtiene reseñas en todos los idiomas
    'day_range': '30',   # Obtiene reseñas de los últimos 30 días
    'num_per_page': 100, # Obtiene 100 reseñas por solicitud
}