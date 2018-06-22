import random


class Edge:
    def __init__(self, destination):
        self.destination = destination


class Vertex:
    def __init__(self, value, color, **pos):
        self.value = value
        self.color = color
        self.pos = pos
        self.edges = []


class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('p1', 'skyblue', x=40, y=40)
        debug_vertex_2 = Vertex('p2', 'blue', x=140, y=140)
        debug_vertex_3 = Vertex('p3', 'green', x=350, y=150)
        debug_vertex_4 = Vertex('p4', 'red', x=300, y=400)
        debug_vertex_5 = Vertex('p5', 'brown', x=300, y=150)

        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)

        debug_edge_2 = Edge(debug_vertex_3)
        debug_vertex_2.edges.append(debug_edge_2)

        debug_edge_3 = Edge(debug_vertex_4)
        debug_vertex_3.edges.append(debug_edge_3)

        debug_edge_4 = Edge(debug_vertex_5)
        debug_vertex_4.edges.append(debug_edge_4)

        self.vertexes.extend(
            [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4, debug_vertex_5])

    def bfs(self, start):
        # colors in Bokeh should be strings, e.g. recognizable color names or hex
        random_color = "#" + \
            ''.join([random.choice('0123456789ABCDEF') for j in range(6)])

        queue = []
        found = []

        queue.append(start)
        found.append(start)

        start.color = random_color

        while len(queue) > 0:
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
            queue.pop(0)  # TODO: look at collection.dequeue
        # return found

    def connected_components(self):
        searched = []
        for vertex in self.vertexes:
            if vertex not in searched:
                searched = self.bfs(vertex)
                # searched.append(self.bfs(vertex))
