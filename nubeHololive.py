import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# ? Importamos las funciones propias del programa
from common.utilities import texto as txt

# Supongamos que tu DataFrame se llama 'df' y la columna que quieres usar se llama 'mi_columna'
df = pd.read_excel('reviews hololive.xlsx')  # Lee el Excel en un DataFrame

# Combina todas las palabras en una gran cadena de texto
texto = ' '.join(df['review'].astype(str))
texto = txt.limpiar_tweets(texto).replace("game", "")

# Crea el Word Cloud
wc = WordCloud(width=800, height=400, background_color='white').generate(texto)

# Muestra el Word Cloud
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
