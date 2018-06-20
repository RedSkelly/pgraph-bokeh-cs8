import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

from graph import *

N = 8
node_indices = list(range(N))

graph_data = Graph()
graph_data.debug_create_test_data()

COLORS = []

for vertex in graph_data.vertexes:
    COLORS.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(COLORS, 'color')
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color='color')

# draw edges from one point to another
graph.edge_renderer.data_source.data = dict(
    start=[0, 1, 2],
    end=[1, 2, 3]
    # start=[node_indices],
    # end=[node_indices]
)

# start of layout code
# circ = [i*2*math.pi/8 for i in node_indices]
# x = [math.cos(i) for i in circ]
# y = [math.sin(i) for i in circ]

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

# print(graph_data.vertexes)


graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
