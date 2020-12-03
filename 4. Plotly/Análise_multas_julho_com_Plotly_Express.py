import plotly.express as px
import pandas as pd

base = pd.read_csv('multas_julho.csv', sep=';')

#Gráfico Gravidade x Veículo x Data
fig = px.scatter(base, x='tipo_veiculo', y='grav_tipo', color='cometimento')
fig.show()

# Gráfico de Barras
multas_por_gravidade = base[['grav_tipo', 'tipo_infracao']]
multas_por_gravidade = multas_por_gravidade['grav_tipo'].value_counts().reset_index()
multas_por_gravidade = multas_por_gravidade.rename(columns={'index':'Gravidade',
                                                            'grav_tipo':'Qtde_infração'})
fig=px.bar(multas_por_gravidade, x='Gravidade', y='Qtde_infração', title='Multas por categ.')
fig.show()

#Gráfico Barras Empilhadas
multas_gravidade_veiculo = base.groupby(["tipo_veiculo", "grav_tipo"]).size().to_frame('size').reset_index()
fig = px.bar(multas_gravidade_veiculo.head(30), x='grav_tipo', y='size', color='tipo_veiculo', 
             title='Total de multas por Gravidade')
fig.show()

#Gráfico de Pizza
multas_por_dia = base.groupby(base['cometimento'])['grav_tipo'].count().reset_index()
multas_por_dia = multas_por_dia.head(10)
multas_por_dia = multas_por_dia.rename(columns = {'grav_tipo':'qtde'})
fig = px.pie(multas_por_dia, values='qtde', names='cometimento', title='Multas por Dia')
fig.show()

#Gráfico de Linha
qtde_dia = base.groupby(base['cometimento'])['tipo_infracao'].count().reset_index()
qtde_dia = qtde_dia.rename(columns={'tipo_infracao':'qtde'}).head(10)
fig=px.line(qtde_dia,x='cometimento', y='qtde',title='Multas por Dia')
fig.show() 

#Histograma
base_hist = base[['tipo_infracao', 'tipo_veiculo', 'grav_tipo']].head(100)
fig = px.histogram(base_hist, x='tipo_veiculo')
fig.show()

#Boxplot
base_box = base.tail(5000)
fig = px.box(base_box, x='grav_tipo', y='tipo_infracao', color='cometimento')
fig.show()