import pandas as pd

base=pd.read_csv('multas_julho.csv', sep=';')

# Qual é o total de infrações por tipo de infração (leve, média, grave, gravíssima)?
total_por_gravidade = base.groupby('grav_tipo').count()[['tipo_infracao']]

# Qual é o total de infrações por dia?
total_por_dia = base.groupby('cometimento').count()[['tipo_infracao']]

# A base de dados possui valores faltantes?
valores_faltantes = base.isna()
base = base.fillna('----')