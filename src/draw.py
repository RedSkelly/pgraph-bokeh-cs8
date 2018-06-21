import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

from graph import *

COLORS = []

graph_data = Graph()
graph_data.debug_create_test_data()

N = len(graph_data.vertexes)    # no longer fixed number of vertices
node_indices = list(range(N))
# print('node_indices: ', node_indices)

# draw edges from one point to another
start_points = []
end_points = []
for vertex in graph_data.vertexes:
    COLORS.append(vertex.color)
    if len(vertex.edges) > 0:
        for edge in vertex.edges:
            start_points.append(graph_data.vertexes.index(vertex))
            end_points.append(graph_data.vertexes.index(edge.destination))

plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(COLORS, 'color')
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color='color')

# draw edges from one point to another, cont.
graph.edge_renderer.data_source.data = dict(
    start=start_points,
    end=end_points
    # start=[0]*N,
    # end=[node_indices]
)
# print('graph.edge_renderer.data_source.data: ',
#       graph.edge_renderer.data_source.data)

# start of layout code
# circ = [i*2*math.pi/8 for i in node_indices]
# x = [math.cos(i) for i in circ]
# y = [math.sin(i) for i in circ]

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

# print('graph_data.vertexes: ', graph_data.vertexes)

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
