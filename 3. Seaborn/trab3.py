import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

base=pd.read_csv('multas_julho.csv', sep=';')

sns.relplot(x='tipo_infracao', y='tipo_veiculo', hue='cometimento', data=base)

fig=plt.subplots(figsize=(12,5))
sns.scatterplot(x='tipo_infracao', y='grav_tipo', hue='tipo_infrator', data=base)

fig=plt.subplots(figsize=(15,7))
sns.scatterplot(x='tipo_veiculo', y='tipo_infracao', hue='grav_tipo', palette="PuOr", data=base)

sns.catplot(x="grav_tipo", kind="count", palette='Blues', data=base)

