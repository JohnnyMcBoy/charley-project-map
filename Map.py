import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('charley.csv')
#df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)

fig = go.Figure(data=go.Scattergeo(
        lon = df['newLong'],
        lat = df['newLat'],
        #text = df['text'],
        mode = 'markers',
        marker_size = 8,
        marker_color = "rgb(255, 0, 0)",
        marker_line = dict(color = "rgb(0, 0, 0)" , width=0.5)
        ))

fig.update_layout(
        title = 'Most trafficked US airports<br>(Hover for airport names)',
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
fig.show()
