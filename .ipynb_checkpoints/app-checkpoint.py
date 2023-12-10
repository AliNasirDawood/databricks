import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output, State
import urllib.parse
import json

dtype_mapping = {'label': 'int'}
path = 'test_data.csv'

df = pd.read_csv(f"{path}")

if 'label' not in df.columns:
    df['label'] = ""

app = dash.Dash(__name__)

candlestick = go.Candlestick(x=df['timestamp'], open=df['open'], high=df['high'], low=df['low'], close=df['close'], text=df['label'], hoverinfo='text')

app.layout = html.Div([
    dcc.Graph(
        id='candlestick-chart',
        figure={'data': [candlestick],
                'layout': {'height': 600,
                           'xaxis': {'rangeslider': {'visible': False}},  # Disable the rangeslider
                           'yaxis': {'rangemode': 'auto'},  # Autoscale the y-axis
                           }
                }
    ),
    html.Div([
        dcc.Input(id='new-label', placeholder='Enter new label', type='text')
    ]),
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=df['timestamp'].min(),
        end_date=df['timestamp'].max(),
        display_format='YYYY-MM-DD'
    ),
    html.Button("Save", id="save-button", n_clicks=0),
    html.Br(),
    html.A(id="download-link", children="Download Data", download="data.csv", href=""),
    html.Div(id='date-range-store', style={'display': 'none'}),
    html.Div(id='label-updated', style={'display': 'none'}),
])

@app.callback(
    Output('date-range-store', 'children'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')
)
def update_date_range(start_date, end_date):
    return json.dumps({'start_date': start_date, 'end_date': end_date})

@app.callback(
    Output('label-updated', 'children'),
    [Input('candlestick-chart', 'clickData'),
     Input('new-label', 'value')]
)
def update_label_in_memory(clickData, new_label):
    if clickData:
        point_ind = clickData['points'][0]['pointIndex']
        df.at[point_ind, 'label'] = new_label
    return new_label

@app.callback(
    Output('candlestick-chart', 'figure'),
    [Input('candlestick-chart', 'clickData'),
     Input('new-label', 'value'),
     Input('date-range-store', 'children'),
     Input('label-updated', 'children')]
)
def update_chart_and_label(clickData, new_label, date_range_json, updated_label):
    date_range = json.loads(date_range_json)
    filtered_df = df[(df['timestamp'] >= date_range['start_date']) & (df['timestamp'] <= date_range['end_date'])]

    if updated_label:
        filtered_df['label'] = updated_label

    candlestick = go.Candlestick(x=filtered_df['timestamp'], open=filtered_df['open'], high=filtered_df['high'],
                                 low=filtered_df['low'], close=filtered_df['close'], text=filtered_df['label'],
                                 hoverinfo='text')

    return {'data': [candlestick], 'layout': {'height': 600, 'xaxis': {'rangeslider': {'visible': False}},
                                               'yaxis': {'rangemode': 'auto'}}}

@app.callback(
    Output("download-link", "href"),
    [Input("save-button", "n_clicks")]
)
def update_download_link(n_clicks):
    if n_clicks is None:
        return ""
    # Save the entire DataFrame to a CSV file, overwriting the previous file
    df.to_csv(f"{path}", index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(df.to_csv(index=False, encoding='utf-8'))
    return csv_string

if __name__ == '__main__':
     app.run_server(port=8136, debug=True)  # Change to an available port