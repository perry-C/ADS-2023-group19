"""
This file contains a number of functions to generate pyplot graph in the form of html strings,
which can then be used for rendering onto template webpages by 'views.py'
"""


import numpy as np
import pandas as pd
import plotly.colors as pc
import plotly.express as px
import plotly.graph_objs as go
from django.http import HttpResponse
from django.shortcuts import render
from plotly.offline import plot

from .models import GraphVisRefugeeData


def make_bar_chart():
    """
    Returns:
        str: a html div string with the a bar chart enclosed inside
    """

    column_names = ["country_of_origin_iso", "total_refugees", "year"]

    qs = GraphVisRefugeeData.objects.values_list(*column_names)

    df = pd.DataFrame(qs, columns=column_names)

    fig = go.Figure()

    for country in df["country_of_origin_iso"].unique()[:5]:
        country_df = df.loc[df["country_of_origin_iso"] == country]
        fig.add_trace(
            go.Histogram(
                x=country_df.loc[:, "year"],
                y=country_df.loc[:, "total_refugees"],
                name=country,
            )
        )

    bar_chart = plot(fig, output_type="div")

    return bar_chart


def make_world_map():
    # df = pd.read_csv(
    #     'https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

    column_names = [
        "country_of_asylum",
        "country_of_origin_iso",
        "country_of_asylum_iso",
        "total_refugees",
        "year",
    ]

    # for now just manually filter cooi to be AFG

    # TODO: later change the ISO to be soemthing selectable

    qs = GraphVisRefugeeData.objects.values_list(*column_names).filter(
        country_of_origin_iso="AFG"
    )

    df = pd.DataFrame(qs, columns=column_names)

    # TODO: convert graph so can be controlled with a slider for time line selection

    fig = go.Figure()

    start_year = df["year"].min()
    end_year = df["year"].max()

    figs = []

    for y in range(start_year, end_year + 1):
        filtered_df = df[df["year"] == y]

        total_refugees = filtered_df["total_refugees"]

        total_refugees_pct = total_refugees / sum(total_refugees)

        # TODO: change this to percentage scale

        total_refugees_pct_log = np.log10(total_refugees_pct)

        ticktext = np.geomspace(total_refugees_pct.min(), total_refugees_pct.max(), 10)

        ticktext = [float(x) * 100 for x in ticktext]

        ticktext = [
            np.format_float_positional(
                x, precision=1, unique=False, fractional=False, trim="k"
            )
            for x in ticktext
        ]

        ticktext = [f"{x}%" for x in ticktext]

        tickvals = np.geomspace(
            total_refugees_pct_log.min(), total_refugees_pct_log.max(), 10
        )

        choropleth = go.Choropleth(
            locations=filtered_df["country_of_asylum_iso"],
            z=total_refugees_pct_log,
            text=total_refugees_pct,
            colorscale="viridis",
            autocolorscale=False,
            reversescale=True,
            colorbar=dict(
                title={
                    "text": "Refugee Count",
                    "font": dict(
                        size=15,
                    ),
                },
                x=0.95,
                tickvals=tickvals,
                ticktext=ticktext,
            ),  
            marker_line_color="darkgray",
            marker_line_width=1.2,
            visible=False,
            hoverinfo="location+text",
        )

        figs.extend([choropleth])

    fig.add_traces(figs)

    # Highlight origin country on the map
    fig.add_trace(
        go.Choropleth(
            locations=["AFG"],
            z=[0],
            colorscale=[[0, "red"], [1, "red"]],
            colorbar=None,
            showscale=False,
            visible=True,
            hoverinfo="location",
        ),
    )

    # Show newest data by default
    fig.data[-2].visible = True

    # Create and add slider
    base_title = "The proportion of Afghan Refugees settling in countries around the world (2015-2022)"
    steps = []
    for i in range(len(fig.data)):
        title = f"{base_title} - Year: {start_year + i}"
        step = dict(
            method="update",
            args=[
                {"visible": [False] * len(fig.data)},
                {"title": title},
            ],  # layout attribute
            label=str(start_year + i),
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        step["args"][0]["visible"][-1] = True  # Toggle AFG (last one) to "visible"

        if len(steps) != len(fig.data) - 1:
            steps.append(step)

    sliders = [
        dict(
            active=end_year - start_year,
            currentvalue={"prefix": "Current Year: "},
            pad={"t": 50},
            steps=steps,
        )
    ]

    fig.update_layout(
        title_text=base_title,
        geo=dict(
            showframe=True, showcoastlines=False, projection_type="equirectangular"
        ),
        # annotations=[dict(
        #     x=0.55,
        #     y=0.1,
        #     xref='paper',
        #     yref='paper',
        #     text='Source: <a href="https://www.unhcr.org/refugee-statistics/download/?url=2bxU2f">\
        #             UNHCR Refugee Data Finder</a>',
        #     showarrow=False
        # )],
        sliders=sliders,
    )

    # fig.update_traces(hovertemplate=f'<extra></extra>')

    world_map = plot(
        fig,
        output_type="div",
    )

    world_map = world_map.replace("<div", '<div class="graph"')

    return world_map
