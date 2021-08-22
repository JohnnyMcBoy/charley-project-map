import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datetime import datetime

df = pd.read_csv('charley.csv')

Date=df['Missing From']
SizeDate=len(Date)
SDate=[' ']*SizeDate
d=[' ']*SizeDate
WordDate=[' ']*SizeDate
x=0
for i in Date:
    SDate[x]=str(Date[x])
    d[x] = datetime.strptime(SDate[x], '%m/%d/%Y')
    WordDate[x]=d[x].strftime('%d, %B %Y')
    x = x+1

df['text'] = df['Location'] + '\n' +  'Name: ' + df['Name'] + '\n' +  ' Sex: ' + df['Sex'] + '\n' +  ' Missing From: ' + WordDate

# FIG
fig = go.Figure(data=go.Scattergeo(
        lon = df['Long'],
        lat = df['Lat'],
        text = df['text'],
        mode = 'markers',
        marker_size = 4,
        marker_color = "rgb(255, 0, 0)",
        marker_line = dict(color = "rgb(0, 0, 0)" , width=0.25)
        ))

fig.update_layout(
    margin=go.layout.Margin(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
    ),
    title = 'Missing People, Cold Cases',
    geo = dict(
        scope = 'world',
        showland = True,
        landcolor = "rgb(64, 64, 64)",
        #subunitcolor = "rgb(0, 255, 0)",
        countrycolor = "rgb(255, 255, 255)",
        showlakes = True,
        lakecolor = "rgb(255, 255, 255)",
        showsubunits = True,
        showcountries = True,

        showocean=True, oceancolor="rgb(250, 250, 250)",
        
        resolution = 50,
        projection = dict(
            #type = 'conic conformal',
            type = 'bonne',
            rotation_lon = -100
        ),
        lonaxis = dict(
            showgrid = True,
            gridwidth = 0.25,
            range= [ -140.0, -55.0 ],
            dtick = 10
        ),
        lataxis = dict (
            showgrid = True,
            gridwidth = 0.25,
            range= [ 20.0, 60.0 ],
            dtick = 5
        )
    )
)
# fig.show()
# FIG ENDS

# DASH APP STARTS
app = dash.Dash(__name__)

app.title = 'Charley Project Map'

app.layout = html.Div(
    className="container", 
    style={
        "width": "80vw",
        'maxWidth': '1000', 
        "margin": "30px auto"
        },
    children=[
        html.Header(
            style={
                'display': 'flex',
                'flex-wrap': 'wrap',
                'paddingBottom': '30',
                'borderBottom': '1px solid black'
            },
            children=[
                html.H1(
                    style={
                        'fontFamily': 'Arial, Helvetica, sans-serif',
                        'wordSpacing': '100vw',
                        'flex': '0 1 20%',
                        'paddingRight': '20'
                    },
                    children=[
                        html.Span(
                            "The "
                        ),
                        html.Span (
                            "Charley ", 
                            style={"color": "red"}
                        ),
                        html.Span(
                            "Project "
                        ),
                        html.Span (
                            "Map", 
                            style={"color": "#565656"}
                        )
                    ]
                ),
                html.P(
                    style={
                        'fontFamily': 'Arial, Helvetica, sans-serif', 
                        "fontSize": "16", 
                        "lineHeight": "1.5",
                        'flex': '0 1 70%',
                        'align-self': 'flex-end'},
                    children=[
                        'The Charley Project profiles over 14,000 “cold case” missing people mainly from the United States. It does not actively investigate cases; it is merely a publicity vehicle for missing people who are often neglected by the press and forgotten all too soon. (Source: ',
                        html.A(
                            children=['The Charley Project'],
                            href="https://charleyproject.org/",
                            style={'color': 'red'}
                        ), 
                        ').'
                    ]
                )
            ]
        ),
        html.Div(
            className="map-container", 
            children=[
                dcc.Graph(
                    id="map",
                    figure=fig
                )
            ]
        )
    ]
)
# DASH APP ENDS


# Set debug to True, so server doesn't have to refresh everytime we change something
if __name__ == '__main__':
    app.run_server(debug=True)
