import pandas as pd
import plotly.graph_objs as go
from django.http import HttpResponse
from django.shortcuts import render
from plotly.offline import plot

from .graphs import make_bar_chart, make_world_map
from .models import GraphVisRefugeeData


def index(request):

    # Handle graph switching resquest

    try:
        selected_graph = request.POST['graph_select']
    except:
        # Default case show world map
        graph = make_world_map()
        return render(request, "graph_vis/index.html", context={"graph": graph})

    else:
        if selected_graph == "bar_chart":
            graph = make_bar_chart()

        elif selected_graph == "world_map":
            graph = make_world_map()

        return render(request, "graph_vis/index.html", context={"graph": graph})
