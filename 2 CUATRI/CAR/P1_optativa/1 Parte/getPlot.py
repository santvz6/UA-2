import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Datos desde el archivo CSV generado previamente
df = pd.read_csv('count.csv')

# Convertir la columna de timestamps a objetos datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y%m%d_%H%M%S')


plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['person_count'], marker='o', linestyle='-', color='teal')

plt.title('Cantidad de Personas Detectadas por Frame a lo Largo del Tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Cantidad de Personas')
plt.grid(True)

plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.tight_layout()

plt.savefig("count.png")
plt.show()