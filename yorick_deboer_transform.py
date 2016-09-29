"""
Yorick de Boer
10786015
Python 3
"""

import networkx as nx

import pydot


def nodes_to_alphatic_list(G):
    return sorted(G.nodes(0))


def get_node_alphabetic_index(G, label):
    return nodes_to_alphatic_list(G).index(label)


def get_node_from_alphabetic_index(G, index):
    return nodes_to_alphatic_list(G)[index]


if __name__ == '__main__':
    G = nx.read_gml('Aarnet.gml')

    sorted_nodes = sorted(G.nodes(0))
    print(sorted_nodes)
    graph = pydot.Dot(graph_type='graph')
    for e in G.edges():
        edge = pydot.Edge(sorted_nodes.index(e[0]), sorted_nodes.index(e[1]))
        graph.add_edge(edge)

    graph.write_png('yorick-deboer-transform.png')
