import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

df=pd.read_csv("map_data_full.csv")
fig=px.density_mapbox(df, lat="latitude", lon="longitude", z="population", radius=20,
                      center=dict(lat=df.latitude.mean(), lon=df.longitude.mean()), zoom=3,
                      mapbox_style='open-street-map', height=900)
fig.show()




app = dash.Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    html.H1("US Population Heatmap", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)