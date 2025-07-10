'''
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load your dataset
df = pd.read_csv("student_data.csv")

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Student Data Bar Chart"

# Layout
app.layout = html.Div([

    html.H2("📊 Student Data Comparison", style={"textAlign": "center"}),

    html.Div([
        html.Label("X-axis: Category", style={"fontWeight": "bold"}),
        dcc.RadioItems(
            id='xaxis_raditem',
            options=[
                {'label': 'Department', 'value': 'Department'},
                {'label': 'Semester', 'value': 'Semester'},
                {'label': 'Gender', 'value': 'Gender'},
                {'label': 'Month', 'value': 'Month'}
            ],
            value='Department',
            style={"width": "50%"}
        )
    ], style={'padding': '20px'}),

    html.Div([
        html.Label("Y-axis: Value to Compare", style={"fontWeight": "bold"}),
        dcc.RadioItems(
            id='yaxis_raditem',
            options=[
                {'label': 'CGPA', 'value': 'CGPA'},
                {'label': 'Project Score', 'value': 'Project Score'},
                {'label': 'Exam Score', 'value': 'Exam Score'},
                {'label': 'Attendance (%)', 'value': 'Attendance (%)'}
            ],
            value='CGPA',
            style={"width": "50%"}
        )
    ], style={'padding': '20px'}),

    html.Div([
        dcc.Graph(id='the_graph')
    ])
])

# Callback to update the graph
@app.callback(
    Output('the_graph', 'figure'),
    [Input('xaxis_raditem', 'value'),
     Input('yaxis_raditem', 'value')]
)
def update_graph(x_axis, y_axis):
    # Group and average the y-values for bar chart
    grouped_df = df.groupby(x_axis)[y_axis].mean().reset_index()

    fig = px.bar(
        grouped_df,
        x=x_axis,
        y=y_axis,
        title=f"Average {y_axis} by {x_axis}",
        color=x_axis
    )

    fig.update_layout(
        xaxis={'categoryorder': 'total ascending'},
        title={'x': 0.5, 'xanchor': 'center'}
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
'''