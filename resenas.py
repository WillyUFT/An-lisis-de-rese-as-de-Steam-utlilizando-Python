# ! Este archivo recogerá las reviews de Steam de juegos Metroidvania

# ^^ Para esta sección se utilizan los datos de SteamSpy,
# ^^ el autor autoriza el uso de su API para esta tesis.

# ? Importamos los paquetes importantes.
import requests
import itertools

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

# * Se crea un diccionario vacío con el propósito de guardar únicamente
# * el título del juego y el AppID.
juegos = {}

# * Para llenarlo se necesitan dos listas
juegos_id = []
juegos_nombre = []

# & Se llenan las listas con los nombres y los id de los juegos.
for app_id, app_info in data.items():
    juegos_id.append(app_id)
    juegos_nombre.append(app_info['name'])
    
# & Se arma el diccionario
for juego_id, juego_nombre in zip(juegos_id, juegos_nombre):
    juegos[juego_id] = juego_nombre

print(juegos)
