import networkx as nx
import yorick_deboer_distance as y_distance


def all_distances(G, path):
    all_distances = dict()
    for start_node in G.nodes(0):
        for goal_node in G.nodes(0):
            all_distances[(start_node, goal_node)] = path.shortest_path_distance(start_node, goal_node)
    return all_distances

def diameter_network(distances):
    max_key = max(distances, key=distances.get)
    return max_key, distances[max_key]

if __name__ == '__main__':
    G = nx.read_gml('Aarnet.gml')
    path = y_distance.Path(G)
    distances = all_distances(G, path)
    diameter = diameter_network(distances)
    print('network diameter is: ' + str(diameter))
    print('path between diameter is: ' + str(path.search(diameter[0][0], diameter[0][1])))