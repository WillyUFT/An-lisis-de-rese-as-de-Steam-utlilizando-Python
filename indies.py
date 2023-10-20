
# ? Importamos los librerías.
import requests
import pandas


# * Creamos la url que sirve para ir a buscar los juegos por tags,
# * El parámetro puede ser cambiado por otro, pero para este caso se
# * necesita "indie".
url = "http://www.steamspy.com/api.php?request=tag&tag=indie"

# * Acá se trae la data.
response = requests.get(url)
data = response.json()

# * Creamos una lista vacía para que almacene unos diccionarios separados.
juegos = []

# & Se llenan las listas con los nombres y los id de los juegos.
for app_id, app_info in data.items():
    juego = {"app_id": app_id, "app_name": app_info["name"]}
    juegos.append(juego)

# * Creamos un dataframe con los juegos que analizaremos
juegos_df = pandas.DataFrame(juegos)

# * Guardar el DataFrame como un archivo de Excel, esto porque el programa se demora demasiado, necesitamos los datos más a la mano
juegos_df.to_excel("juegos indie.xlsx", index=False)

print(juegos_df)