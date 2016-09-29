"""
Yorick de Boer
10786015
Python 3
"""
import networkx as nx

import yorick_deboer_distance as y_distance
from yorick_deboer_transform import get_node_from_alphabetic_index


def all_distances(G, path):
    all_distances = dict()
    for start_node in G.nodes(0):
        for goal_node in G.nodes(0):
            all_distances[(start_node, goal_node)] = path.shortest_path_distance(start_node, goal_node)
    return all_distances


def diameter_network(distances):
    max_key = max(distances, key=distances.get)
    return max_key, distances[max_key]


def distance_1to6(G):
    node1 = get_node_from_alphabetic_index(G, 1)
    node6 = get_node_from_alphabetic_index(G, 6)
    path = y_distance.Path(G)
    return path.distance(node1, node6)


def diameter_network_remove_source6_target12(G):
    """
    TASK 4
    :param G:
    :return:
    """
    node6 = get_node_from_alphabetic_index(G, 12)
    node12 = get_node_from_alphabetic_index(G, 17)
    print('removing edge between ' + node6 + ' and ' + node12)
    G.remove_edge(node6, node12)
    distances = all_distances(G, y_distance.Path(G))
    return diameter_network(distances)


if __name__ == '__main__':
    G = nx.read_gml('Aarnet.gml')
    path = y_distance.Path(G)
    distances = all_distances(G, path)
    diameter = diameter_network(distances)
    print('network diameter is: ' + str(diameter))
    print('path between diameter is: ' + str(path.search(diameter[0][0], diameter[0][1])))
    print()

    distance_1_6 = distance_1to6(G)
    print('distance between 1 and 6 ' + str(distance_1_6))

    x = 0
    for key, value in distances.items():
        if value > distance_1_6:
            x += 1
    print('amount of pairs exceed ' + str(x) + ' off total ' + str(len(distances)))
    print()

    print("TASK 4:")
    print('diameter without edge 6->12 ' + str(diameter_network_remove_source6_target12(G)))
