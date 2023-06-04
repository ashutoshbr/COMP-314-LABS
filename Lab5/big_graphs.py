import matplotlib.pyplot as plt
import networkx as nx
from small_graph import (
    get_nodes_edges,
    get_avg_degree,
    get_density,
    get_diameter,
    clustering_coefficients,
    avg_cc,
)


def plot_degree_dist(G):
    degree_dist = {}
    node_count = len(G.nodes())
    print(node_count)
    for n in G.nodes():
        degree = G.degree(n)
        if degree not in degree_dist:
            degree_dist[degree] = 1
        else:
            degree_dist[degree] += 1

    for k, v in degree_dist.items():
        degree_dist[k] = v / node_count
    plt.bar(degree_dist.keys(), degree_dist.values())
    plt.xlabel("Degree")
    plt.ylabel("Fraction of nodes")
    plt.show()


Graph1 = nx.read_weighted_edgelist(
    "./Lab5/rt_onedirection/rt_onedirection.edges", delimiter=","
)
Graph2 = nx.read_weighted_edgelist("./Lab5/rt_saudi/rt_saudi.edges", delimiter=",")
Graph3 = nx.read_weighted_edgelist(
    "./Lab5/rt_barackobama/rt_barackobama.edges", delimiter=","
)
Graph4 = nx.read_weighted_edgelist("./Lab5/rt_http/rt_http.edges", delimiter=",")
Graph5 = nx.read_weighted_edgelist("./Lab5/rt_libya/rt_libya.edges", delimiter=",")

GRAPHS = {
    "rt_onedirection": Graph1,
    "rt_saudi": Graph2,
    "rt_barackobama": Graph3,
    "rt_http": Graph4,
    "rt_libya": Graph5,
}

# Func calls from small_graph
for name, graph in GRAPHS.items():
    print(f"Graph: {name}")
    print("G(V,E): ", get_nodes_edges(graph))
    print("Avg degree: ", get_avg_degree(graph))
    print("Density: ", get_density(graph))
    print("Diameter: ", get_diameter(graph))
    clustering_coeffs = clustering_coefficients(graph)
    print("Avg clustering coefficient:", avg_cc(clustering_coeffs))
    print("-----------------------")
    nx.draw(graph)
    plt.show()
    plot_degree_dist(graph)
