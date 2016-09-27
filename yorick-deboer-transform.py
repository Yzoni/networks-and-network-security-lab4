import networkx as nx

import pydot

if __name__ == '__main__':
    G = nx.read_gml('Aarnet.gml')

    sorted_nodes = sorted(G.nodes(0))
    graph = pydot.Dot(graph_type='graph')
    for e in G.edges():
        edge = pydot.Edge(sorted_nodes.index(e[0]), sorted_nodes.index(e[1]))
        graph.add_edge(edge)

    graph.write_png('yorick-deboer-transform.png')
