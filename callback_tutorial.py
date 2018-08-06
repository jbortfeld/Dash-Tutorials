import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

app = dash.Dash()


df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

app.layout = html.Div([

    html.H1(children = 'MY MAIN TITLE'),

    html.Div(children = 'Hello, this is a test of the dash framework. '
                        'I will here test the callback feature.'),

    html.Div(children = 'Blah blah blah'),

    # this is a text box that is identitied by "id='my_id'"
    # when it first starts the value inside the text box will be'initial value'
    # this is the input to the callback
    dcc.Input(id='my-id', value='initial value', type='text'),

    # this will be where the callback output goes
    # we will use whatever gets returned by the function that follows
    # the @app.callback where the output component_id = 'my_div'
    # in this case, the output is a string
    html.Div(id='my-div'),

    # this will create a scatterplot
    dcc.Graph(
            id='life-exp-vs-gdp',
            figure={
                'data': [
                    go.Scatter(
                        x=df[df['continent'] == i]['gdp per capita'],
                        y=df[df['continent'] == i]['life expectancy'],
                        text=df[df['continent'] == i]['country'],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=i
                    ) for i in df.continent.unique()
                ],
                'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                    yaxis={'title': 'Life Expectancy'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )

])

#####################
# callback # 1
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)
# end callback 1
#####################


if __name__ == '__main__':
    app.run_server()