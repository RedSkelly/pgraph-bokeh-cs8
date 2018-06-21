import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Range1d, LabelSet, Label
from bokeh.palettes import Spectral8

from graph import *

# TODO: graph renders as square even if height != width
# WIDTH = 640
# HEIGHT = 480
# maybe plot_width=WIDTH plot_height=HEIGHT in plot=figure() below
CIRCLE_SIZE = 30
COLORS = []

graph_data = Graph()
graph_data.debug_create_test_data()
graph_data.bfs(graph_data.vertexes[0])

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

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(COLORS, 'color')
graph.node_renderer.glyph = Circle(size=CIRCLE_SIZE, fill_color='color')

graph.edge_renderer.data_source.data = dict(
    start=start_points,
    end=end_points
)
# print('graph.edge_renderer.data_source.data: ',
#       graph.edge_renderer.data_source.data)

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]
# print('graph_data.vertexes: ', graph_data.vertexes)

# start of layout code
graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)
plot.renderers.append(graph)

# create a new dict to use as a data source, with three lists in it, ordered in the same way as vertexes
# list of x value
# list of y values
# list of labels

# TODO: possible optimization: we run through this loop three times
value = [v.value for v in graph_data.vertexes]

label_source = ColumnDataSource(data=dict(x=x, y=y, v=value))

labels = LabelSet(x='x', y='y', text='v', level='glyph', source=label_source,
                  render_mode='canvas', text_align='center', text_baseline='middle', text_color='white')

# TODO: investigate: plot.add_layout() vs plot.renderers.append()
plot.add_layout(labels)

output_file('graph.html')
show(plot)
