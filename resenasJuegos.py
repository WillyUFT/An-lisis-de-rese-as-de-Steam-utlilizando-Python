# ! Este archivo recogerá las reviews de Steams de varios estilos

# * ========================================================================= #
# *                               IMPORTACIONES                               #
# * ========================================================================= #
import pandas
import steamreviews
import json

# * ========================================================================= #
# *                                 VARIABLES                                 #
# * ========================================================================= #

listaJuegos = [
    "prueba",
    "juegos_cute",
    "juegos_anime",
    "juegos_indie",
    "juegos_metroidvania",
    "juegos_female+protagonist",
]

request_params = {"language": "english,spanish", "num_per_page": "100"}  # Máximo es 100

limite_de_resenas = 2000
reseñas = []

# * ========================================================================= #
# *                          BUSCAR TODAS LAS RESEÑAS                         #
# * ========================================================================= #

for nombrejuego in listaJuegos:
    with open("data/listaJuegos/" + nombrejuego + ".json", "r") as file:
        juegos_data = json.load(file)

    juegos_df = pandas.DataFrame.from_dict(juegos_data, orient="index")
    juegos_a_buscar = juegos_df["appid"].tolist()

    print("Vamos a bsucar los juegos de este json " + nombrejuego)

    for app_id in juegos_a_buscar:
        review_dict, query_count = steamreviews.download_reviews_for_app_id(
            app_id,
            chosen_request_params=request_params,
            limite_resenas=limite_de_resenas,
        )
        reseñas_temporales = []

        # * Itera sobre las reseñas descargadas y detente si alcanzamos el límite
        for review_id in review_dict["reviews"]:
            if len(reseñas_temporales) < limite_de_resenas:
                review_data = review_dict["reviews"][review_id]
                reseñas_temporales.append(review_data)
            else:
                # * Nos detenemos cuando llegamos al límite
                break

        reseñas.extend(reseñas_temporales)

        reseñas_df = pandas.DataFrame(reseñas)
        reseñas_df.to_excel(nombrejuego + ".xlsx", index=False)
