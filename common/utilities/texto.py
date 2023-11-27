
# ! Importamos las cosas necesarias.
import re  # Expresiones regulares
import emoji  # Esto es para eliminar los emojis
import string
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Creamos un pool de stopwords para no tener que andar vaalidando el idioma
stop_words_es = set(stopwords.words('spanish'))
stop_words_en = set(stopwords.words('english'))
palabras_adicionales = ["game", "suisex"]
stop_words = stop_words_es.union(stop_words_en)
stop_words.update(palabras_adicionales)


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
    tweet_limpio = eliminar_emojis(tweet_limpio)

    return tweet_limpio

def eliminar_emojis(texto):
    # Patrón de regex para identificar emojis
    patron_emoji = re.compile("["
                         u"\U0001F600-\U0001F64F"  # emoticones
                         u"\U0001F300-\U0001F5FF"  # símbolos y pictogramas
                         u"\U0001F680-\U0001F6FF"  # símbolos de transporte y mapas
                         u"\U0001F1E0-\U0001F1FF"  # banderas (iOS)
                         u"\U00002702-\U000027B0"
                         u"\U000024C2-\U0001F251"
                         "]+", flags=re.UNICODE)
    return patron_emoji.sub(r'', texto)

def eliminar_stop_words(texto: str) -> str:
    texto_limpio = ' '.join([word for word in texto.split() if word not in stop_words])
    return texto_limpio

def otener_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

def lematizar_texto(texto: str) -> str:
    texto_lematizado = ' '.join([lemmatizer.lemmatize(w, otener_pos(w)) for w in nltk.word_tokenize(texto)])
    return texto_lematizado


def limpieza_total_text(texto: str) -> str:
    # print("\n\nTEXTO ANTIGUO:\n\n" + texto)
    texto_limpio = limpiar_tweets(texto)
    texto_limpio = eliminar_stop_words(texto_limpio)
    texto_limpio = lematizar_texto(texto_limpio)
    # print("\n\nTEXTO LIMPIO:\n\n" + texto_limpio)
    return texto_limpio
    

def es_ascii(s) -> bool:
    return all(c in string.printable for c in s)
