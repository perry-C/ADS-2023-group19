import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from plotly.graph_objs import Scatter
from plotly.offline import plot

from .models import MapVisRefugeedata


def index(request):
    df = pd.DataFrame(MapVisRefugeedata.objects.values_list(
        "total_refugees", "year_field"))
    print(df)

    plot_div = plot([Scatter(x=df.iloc[:, 1], y=df.iloc[:, 0],
                             mode="lines", name="test",
                             opacity=0.8, marker_color="green")],
                    output_type="div")
    return render(request, "map_vis/index.html", context={"plot_div": plot_div})
