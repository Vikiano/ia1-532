import pandas as pd
from dash import Dash, html, dcc, Input, Output
import altair as alt
# alt.data_transformers.enable('data_server')

crime_data = pd.read_csv("https://raw.githubusercontent.com/Vikiano/datasets/main/crimedata_csv_AllNeighbourhoods_2021.csv")
crime_data.head()

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='TYPE',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in crime_data.columns])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(crime_data).mark_point().encode(
        x=xcol,
        y='TYPE',
        tooltip='YEAR').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)