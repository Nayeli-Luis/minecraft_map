# Ver mapa 

import plotly.express as px

coord_df = pd.read_csv("coordenadas.csv")

# Graficar
fig = px.scatter_3d(coord_df, x='x', y='y', z='z',
              color='tipo_lugar', size_max=18,
              symbol='tipo_lugar', opacity=0.7)


fig.show()