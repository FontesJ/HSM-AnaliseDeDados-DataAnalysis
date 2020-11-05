import pandas as pd
import seaborn as sns
import plotly.express as px
base = pd.read_csv('vw_pib_percapita.csv')

# Histograma com a distribuição de dados coletados por Unidade Federativa
fig = px.histogram(base, x='UF', title='Distribuição por Estado')
fig.show()

# Mapa de Calor
sns.heatmap(base.corr(), vmax=1.0, annot=True)

# Gráfico de dispersão UF x PIB per capita
fig = px.scatter(base, x='UF', y='PIB_percapita')
fig.show()

pib_estado = base.groupby('UF').sum()
pib_estado = pib_estado[['Pop_est_2009', 'PIB_percapita']].reset_index()

# Histograma população por estado
fig = px.histogram(pib_estado, x='UF', y='Pop_est_2009', title='PIB por Estado')
fig.show()

#Gráfico de linha PIB per capita por Estado
fig=px.line(pib_estado,x='UF', y='PIB_percapita',title='PIB per capita por Estado')
fig.show()
