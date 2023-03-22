import pandas as pd
import plotly.graph_objs as go
from django.http import HttpResponse
from django.shortcuts import render
from plotly.offline import plot

from .models import MapVisRefugeedata


def index(request):
    df = pd.DataFrame(MapVisRefugeedata.objects.values_list(
        "country_of_origin_iso", "total_refugees", "year"), columns=["country_of_origin_iso", "total_refugees", "year"])

    bar_fig = go.Figure()

    for country in df["country_of_origin_iso"].unique()[:5]:
        country_df = df.loc[df["country_of_origin_iso"] == country]
        bar_fig.add_trace(
            go.Bar(x=country_df.loc[:, "year"], y=country_df.loc[:, "total_refugees"], name=country))

    bar_div = plot(bar_fig,
                   output_type="div")
    return render(request, "map_vis/index.html", context={"bar_div": bar_div})
