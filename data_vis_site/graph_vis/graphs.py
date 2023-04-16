'''
This file contains a number of functions to generate pyplot graph in the form of html strings,
which can then be used for rendering onto template webpages by "views.py"
'''


import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from django.http import HttpResponse
from django.shortcuts import render
from plotly.offline import plot

from .models import GraphVisRefugeeData


def make_bar_chart():
    '''
    Returns:
        str: a html div string with the a bar chart enclosed inside
    '''

    df = pd.DataFrame(GraphVisRefugeeData.objects.values_list(
        "country_of_origin_iso", "total_refugees", "year"), columns=["country_of_origin_iso", "total_refugees", "year"])

    fig = go.Figure()

    for country in df["country_of_origin_iso"].unique()[:5]:
        country_df = df.loc[df["country_of_origin_iso"] == country]
        fig.add_trace(
            go.Histogram(x=country_df.loc[:, "year"], y=country_df.loc[:, "total_refugees"], name=country))

    bar_chart = plot(fig,
                     output_type="div")

    return bar_chart


def make_world_map():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

    fig = go.Figure(data=go.Choropleth(
        locations=df['CODE'],
        z=df['GDP (BILLIONS)'],
        text=df['COUNTRY'],
        colorscale='Blues',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_tickprefix='$',
        colorbar_title='GDP<br>Billions US$',
    ))

    fig.update_layout(
        title_text='2014 Global GDP',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations=[dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
                CIA World Factbook</a>',
            showarrow=False
        )]
    )

    world_map = plot(fig,
                     output_type="div")

    return world_map
