import pandas as pd
import matplotlib as plt

base=pd.read_csv('multas_julho.csv', sep=';')

# O total de infrações por tipo, com o eixo x representando o tipo e o eixo y o total
base["grav_tipo"].value_counts(ascending=False).plot(title="Infrações x Gravidade",
                                                         color="red", marker='o')
plt.xlabel("Gravidade")
plt.ylabel("Quantidade")

# O total de infrações por tipo de infrator, como condutor e proprietário
base["tipo_infrator"].value_counts().plot.pie(title="Infrações x Infrator")
