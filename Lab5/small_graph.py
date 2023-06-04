import matplotlib.pyplot as plt
import networkx as nx

"""
The data is in the form of:
Edge1 Edge2 Weight
X       X       X
X       X       X
X       X       X
...
Ref: https://networkx.org/documentation/stable/reference/readwrite/index.html
"""

G = nx.read_weighted_edgelist(
    "./Lab5/mammalia-bat-roosting-indiana/mammalia-bat-roosting-indiana.edges"
)


def get_nodes_edges(G) -> tuple:
    """
    Number of nodes and edges as a tuple(V, E)
    """
    return (nx.number_of_nodes(G), nx.number_of_edges(G))


def get_avg_degree(G) -> float:
    """
    Average degree = nodes/edges
    """
    return get_nodes_edges(G)[0] / get_nodes_edges(G)[1]


def get_density(G) -> int | float:
    """
    Density: Ratio of the number of edges to the number of possible edges in the network
    """
    num_of_nodes = nx.number_of_nodes(G)
    num_of_edges = nx.number_of_edges(G)
    if num_of_nodes == 0:
        return 0
    else:
        density = (2 * num_of_edges) / (num_of_nodes * (num_of_nodes - 1))
    return density


def get_diameter(G) -> int:
    """
    Diameter: Length of the shortest path between the most distanced nodes
    """
    return nx.diameter(G)


def clustering_coefficients(G) -> dict:
    """
    Clustering coefficients of all the nodes
    """
    clustering_coeffs = {}
    for node in G.nodes:
        neighbours = list(nx.neighbors(G, node))
        k = len(neighbours)
        if k > 1:
            e = 0
            for v in G.adj[node]:
                for u in G.adj[node]:
                    if v == u:
                        continue
                    if G.has_edge(u, v):
                        e += 1
            e = e / 2
            clustering_coeffs[node] = (2 * e) / (k * (k - 1))
        else:
            clustering_coeffs[node] = 0

    return clustering_coeffs


def avg_cc(coefficients: dict) -> float:
    """
    Average of the clustering coefficients
    """
    avg = 0.0
    for value in coefficients.values():
        avg += value
    avg = avg / len(coefficients)
    return avg


if __name__ == "__main__":
    print("num_of_nodes:", get_nodes_edges(G)[0])
    print("num_of_edges:", get_nodes_edges(G)[1])
    print("Average degree:", get_avg_degree(G))
    density = get_density(G)
    print("Density: ", density)
    print("Diameter: ", get_diameter(G))
    avg_clustering_coeffs = avg_cc(clustering_coefficients(G))
    print("Avg Clustering Coefficient: ", avg_clustering_coeffs)

    # Test density
    expected_den = nx.density(G)
    assert density == expected_den
    # Test clustering
    cc = nx.clustering(G)
    expected_avg_cc = sum(cc.values()) / len(cc.values())
    assert avg_clustering_coeffs == expected_avg_cc

    # display graph using defaults
    nx.draw(G)
    plt.show()
