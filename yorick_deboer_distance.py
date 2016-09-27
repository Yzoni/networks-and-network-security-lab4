import networkx as nx
from collections import namedtuple

import pydot
from geopy.distance import vincenty as v_distance
from queue import PriorityQueue


class Path:
    GPS = namedtuple('GPS', ['lat', 'lon'])

    def __init__(self, graph):
        self.graph = graph
        pass

    def distance(self, node_1, node_2):
        """
        Straight line distance between a node and goal node
        """
        GPS_1 = (self.graph.node[node_1]['Latitude'], self.graph.node[node_1]['Longitude'])
        GPS_2 = (self.graph.node[node_2]['Latitude'], self.graph.node[node_2]['Longitude'])
        return v_distance(GPS_1, GPS_2).km

    def search(self, start, goal):

        closed_set = list()
        open_set = PriorityQueue()
        open_set.put(start, 0)

        back_set = dict()
        back_set[start] = None

        cost = float("inf")
        while not open_set.empty():
            current = open_set.get()
            if current == goal:
                return self._get_shortest_path(back_set, goal)

            closed_set.append(current)

            for neighbour in self.graph[current]:
                if neighbour not in closed_set:
                    h_distance = self.distance(neighbour, goal)
                    g_distance = self.distance(neighbour, current)
                    new_cost = h_distance + g_distance
                    if neighbour not in back_set or new_cost < cost:
                        cost = new_cost
                        open_set.put(neighbour, cost)
                        back_set[neighbour] = current
        return []

    def shortest_path_distance(self, start, goal):
        path_list = self.search(start, goal)
        path_list_length = len(path_list)
        distance = 0
        for idx, node in enumerate(path_list):
            if path_list_length is not idx + 1:
                distance += self.distance(path_list[idx], path_list[idx + 1])
        return distance

    def _get_shortest_path(self, backset, goal):
        path = [goal]
        while path[-1] is not None:
            path.append(backset[path[-1]])
        path.reverse()
        return path[1:]


def plot_shortest_path(G, path_list, file_name):
    graph = pydot.Dot(graph_type='graph')
    for e in G.edges():
        if e[0] in path_list and e[1] in path_list:
            edge = pydot.Edge(e[0], e[1], color="red")
        else:
            edge = pydot.Edge(e[0], e[1])
        graph.add_edge(edge)
    graph.write_png(file_name + '.png')

if __name__ == '__main__':
    G = nx.read_gml('Aarnet.gml')
    path = Path(G)
    path_list = path.search('Adelaide1', 'Brisbane1')
    print(path_list)
    print(str(path.shortest_path_distance('Adelaide1', 'Brisbane1')) + ' km')
    plot_shortest_path(G, path_list, 'yorick-deboer-shortestpath')
