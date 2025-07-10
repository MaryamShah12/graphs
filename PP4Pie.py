'''import plotly.express as px
import pandas as pd
# This dataframe has 244 lines, but 4 distinct values for `day`
df = pd.read_csv("student_dataset.csv")
fig = px.pie(df, values='Assignments Score', names='Name')
fig.show()
fig.write_image("image.png")'''

'''
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv("student_data.csv")

# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__)

#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.Label(['Students data']),
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': 'Department', 'value': 'Department'},
                     {'label': 'Semester', 'value': 'Semester'},
                     {'label': 'Gender', 'value': 'Gender'},

            ],
            value='Department',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
    ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

])

#---------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = df

    piechart=px.pie(
            data_frame=dff,
            names=my_dropdown,
            hole=.3,
            )

    return (piechart)


if __name__ == '__main__':
    app.run(debug=True)
'''