from bokeh.io import curdoc, show
from bokeh.models import ColumnDataSource, LinearColorMapper, HoverTool, CustomJS
from bokeh.plotting import figure
from bokeh.palettes import Viridis256

from Hexagon import Hexagon, HexagonGrid 

# Init hexagon grid
RADIUS = 20
hexagon_grid = HexagonGrid(RADIUS)
hexagons = hexagon_grid.hexagons

# Init data source
source = ColumnDataSource(data=dict(
    q=[h.q for h in hexagons.values()],
    r=[h.r for h in hexagons.values()],
    colors=[h.color for h in hexagons.values()]
))

# Create plot
plot = figure(width=800, height=800)

# Create color mapper
color_mapper = LinearColorMapper(palette=Viridis256, low=0, high=1)

# Add hex tile glyphs
glyph = plot.hex_tile(q='q', r='r', fill_color='colors', source=source, line_color=None)

# Set up hover tool
hover = HoverTool()
plot.add_tools(hover)

# Hover callback 
hover_callback = CustomJS(code="""
    // Code to highlight hovered hexagon
""")
hover.callback = hover_callback

# Callback when data changes
def update(attr, old, new):
    source.trigger('change', 'data', old, new)

source.on_change('data', update) 

# Function to update data
def update_data(new_hexagons):
    old_colors = source.data['colors']
    new_colors = [h.color + .1 for h in new_hexagons.values()]

    old_data = source.data
    new_data = dict(
        q=old_data['q'],
        r=old_data['r'],
        colors=new_colors
    )
    source.data = new_data

    source.trigger('change', 'data', old_colors, new_colors)

# Set up layout
curdoc().add_root(plot)

# Display plot
show(plot)

# Initial data
# update_data(hexagons)

# Call update_data(new_data) when data change

