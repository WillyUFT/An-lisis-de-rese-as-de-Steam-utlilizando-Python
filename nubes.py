
# ! Este archivo es el que utilizaremos para hacer la limpieza de los textos

import json
import pandas
from common.utilities import texto as txt
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# lista_resenas = ["anime", "cute", "female+protagonist","indie","metridvania"]
lista_resenas = ["prueba"]

# * Preguntamos que xlsx queremos revisar, para no hacer un for gigante
tag = input("Inserte el tag para limpiar los datos:  ")
print("Buscando el dataframe: " + "juegos_" + tag + ".xlsx")

# * Creamos el dataframe
for etiqueta in lista_resenas:
    data_frame = pandas.read_excel("juegos_" + etiqueta + ".xlsx")
    lista_resenas = data_frame['review'].tolist()
    reseñas_limpias = [txt.limpieza_total_text(str(reseña)) for reseña in lista_resenas]
    df_reseñas_limpias = pandas.DataFrame(reseñas_limpias, columns=['review'])
    df_reseñas_limpias.to_excel("reseñas_limpias_" + etiqueta + ".xlsx", index=False)


# # * Combina todas las palabras en una gran cadena de texto
# texto = ' '.join(reseñas_limpias)

# # Crea el Word Cloud
# wc = WordCloud(width=800, height=400, background_color='white').generate(texto)

# # Muestra el Word Cloud
# plt.figure(figsize=(10, 10))
# plt.imshow(wc, interpolation='bilinear')
# plt.axis('off')
# plt.show()


