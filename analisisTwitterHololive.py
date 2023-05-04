#! Este archivo es para analizar los sentimientos de Hololive por Twitter.

# ? Importamos las librerías y paquetes
import tweepy
import common.config.twitter.twitterAPIConfiguration as twitterConfig
import pandas
import common.utilities.texto as texto
import common.utilities.tiempo as tiempo

# * Primero autenticamos
api = twitterConfig.autenticar_app()

# * Se crea un dataframe para guardar los tweets
tweets_df = pandas.DataFrame(
    columns=["Fecha", "Tweet", "Usuario", "Retweets", "Likes", "Seguidores"]
)

# * Buscamos tweets
tweets_raw = tweepy.Cursor(
    api.search_tweets,
    q=twitterConfig.HOLOLIVE,
    count=100,
    lang="en",
    tweet_mode="extended",
).items(100)

# * Creamos una lista de diccionarios con los tweets que obtuvimos
tweets_list = []

# * Para llenar la lista hacemos lo siguiente:
for tweet in tweets_raw:
    try:
        tweets_list.append(
            {
                "Fecha": tiempo.formatear_fecha(tweet.created_at),
                "Tweet": texto.limpiar_tweets(tweet.full_text),
                "Usuario": tweet.user.screen_name,
                "Retweets": tweet.retweet_count,
                "Likes": tweet.favorite_count,
                "Seguidores": tweet.user.followers_count,
            }
        )
    except AttributeError as e:
        print("Se ha producido un error al extraer la información del tweet: " + str(e))
        continue

# * Creamos el Dataframe
tweets_df = pandas.DataFrame(tweets_list)


