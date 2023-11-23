# ! Este archivo recogerá las reviews de Steams de varios estilos
import pandas
import steamreviews
import json

listaJuegos = [
    "juegos_2D",
    "juegos_action",
    "juegos_anime",
    "juegos_cute",
    "juegos_indie",
    "juegos_metroidvania",
    "juegos_pixel+graphics",
]

for nombrejuego in listaJuegos:
    with open("data/listaJuegos/" + nombrejuego + ".json", "r") as file:
        juegos_data = json.load(file)

    primeras_200_entradas = dict(list(juegos_data.items())[:200])

    with open(nombrejuego + "_200.json", "w") as file:
        json.dump(primeras_200_entradas, file, indent=4)

    juegos_df = pandas.DataFrame.from_dict(primeras_200_entradas, orient="index")
    juegos_a_buscar = juegos_df["appid"].tolist()

    reseñas = []

    for app_id in juegos_a_buscar:
        review_dict = steamreviews.download_reviews_for_app_id(app_id)

        for review_id in review_dict["reviews"]:
            review_data = review_dict["reviews"][review_id]

    reseñas_df = pandas.DataFrame(reseñas)
    reseñas_df.to_excel(nombrejuego + ".xlsx", index=False)
