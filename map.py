from bokeh.io import curdoc, show
from bokeh.models import ColumnDataSource, Grid, HexTile, LinearAxis, Plot
import numpy as np
from Hexagon import Hexagon, HexagonGrid

radius = 5
hexagon_grid = HexagonGrid(radius)
hexagons = hexagon_grid.hexagons

source = ColumnDataSource(data=dict(
    q=[hexagon.q for hexagon in hexagons],
    r=[hexagon.r for hexagon in hexagons],
))

plot = Plot(
    title=None, width=800, height=800,
    min_border=0, toolbar_location=None)

glyph = HexTile(q="q", r="r", size=1, fill_color="#fb9a99", line_color="white")
plot.add_glyph(source, glyph)

xaxis = LinearAxis()
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot.add_layout(yaxis, 'left')

plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

curdoc().add_root(plot)

show(plot)
