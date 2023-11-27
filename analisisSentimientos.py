
# ! Archivo apra el analisis de sentimientos
import matplotlib.pyplot as plt
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Vamos a probar con los indies
df = pd.read_excel("reseñas_limpias_hololive.xlsx")

print(df.head())

analyzer = SentimentIntensityAnalyzer()

# Aplicar VADER a cada reseña y almacenar los resultados
df['sentiment'] = df['review'].apply(lambda x: analyzer.polarity_scores(str(x))['compound'])
df_filtrado = df[df['sentiment'] != 0]

# * hacemos el gráfico
plt.hist(df_filtrado['sentiment'], bins=50, color='#0099bb', alpha=0.7)
plt.title('Distribución de Sentimiento')
plt.xlabel('Puntaje de Sentimiento')
plt.ylabel('Frecuencia')
plt.show()

