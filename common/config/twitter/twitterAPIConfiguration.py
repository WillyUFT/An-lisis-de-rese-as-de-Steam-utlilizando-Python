#!!!!!!!!! Acá únicamente están las variables a cargo de las Keys de Twitter API!!!

# Importamos Tweepy
import tweepy

#! KEYS PARA UTILIZAR LA API

# ? El consumer key es como el ID de la aplicación.
CONSUMER_KEY = "FTWT88VwlUXUMwdOinaQxhkyU"

# ? Este es la clave del ID de la aplicación
CONSUMER_SECRET = "3wxxcwgLJOQcSATBrC1l0m23jqpjX5Rzs7kxl6OAE7Nwcy9Gnr"

# ? Esta es el bearer token para entrar a twitter
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAAZ0nAEAAAAAK94bJBPQEhZozJYmOyanccuyCws%3DrAA2ejQ8EfbiUi2UEU5NwcbqJupkuLalBkXe2WUUT5nXt6uNoP"

# ? Esto corresponde a un caracter que emula un usario en nombre
# ? de la aplicación. En este caso, mi cuenta de Twitter
ACCESS_TOKEN = "1190931243124379649-Ep1t4zyfuj52mrP5kyZGdpEVVeNKcC"

# ? Esta es la contraseña de la usuario del access token
ACCESS_SECRET = "DLckYpV00ozIO5zrZwxJMY0FH2ed51nd4soQmV7Qwu6e9"

CLIENT_ID = "VnR6cDRKeHdTUDE5VXVrVUFUTzY6MTpjaQ"

CLIENT_SECRET = "ymfruxmrJzVZFnlAPEub-8MSFpNrCgfZU-NeYXUMBW2ZPHbNKY"

#! Búsquedas
HOLOLIVE = "Hololive"
METROIDVANIA = "Metroidvania"


#! Autenticación
def autenticar_app():
    cliente = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    cliente.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(cliente)