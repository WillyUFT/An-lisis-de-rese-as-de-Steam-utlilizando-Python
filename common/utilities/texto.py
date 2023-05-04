## Importamos las cosas necesarias.
import re  # Expresiones regulares
import emoji  # Esto es para eliminar los emojis de los tweets


# & Esta función hará que limpiemos los tweets
def limpiar_tweets(tweet: str) -> str:
    """
    Esta función toma un tweet desde Twitter y limpia el texto en él

    Returns:
        str: Tweet limpio sin hashtags, ni links, etc.
    """

    # Eliminar URLs
    tweet_limpio = re.sub(r"http\S+|www\S+|https\S+", "", tweet, flags=re.MULTILINE)

    # Eliminar menciones
    tweet_limpio = re.sub(r"@\w+", "", tweet_limpio)

    # Eliminar números
    tweet_limpio = re.sub(r"\d+", "", tweet_limpio)

    # Eliminar signos de puntuación
    tweet_limpio = re.sub(r"\W", " ", tweet_limpio)

    # Eliminar espacios extra
    tweet_limpio = re.sub(r"\s+", " ", tweet_limpio).strip()

    # Sacar el RT
    tweet_limpio = re.sub(r"\rt+", "", tweet_limpio)

    # Convertir a minúsculas
    tweet_limpio = tweet_limpio.lower()
    
    # Eliminamos los emojis
    tweet_limpio = emoji.get_emoji_regexp().sub("", tweet_limpio)

    return tweet_limpio
