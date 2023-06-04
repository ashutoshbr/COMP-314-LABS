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

# Number of nodes and edges
num_of_nodes = nx.number_of_nodes(G)
num_of_edges = nx.number_of_edges(G)
# Average degree
avg_degree = num_of_edges / num_of_nodes


def get_density(G) -> int | float:
    num_of_nodes = nx.number_of_nodes(G)
    num_of_edges = nx.number_of_edges(G)
    if num_of_nodes == 0:
        return 0
    else:
        density = (2 * num_of_edges) / (num_of_nodes * (num_of_nodes - 1))
    return density


def get_diameter(G) -> int:
    return nx.diameter(G)


def clustering_coefficient(G) -> dict:
    coefficients = {}
    for node in G.nodes:
        degree = len(G.adj[node])
        if degree <= 1:
            coefficients[node] = 0
            continue
        num_edges = 0
        for v in G.adj[node]:
            for u in G.adj[node]:
                if v == u:
                    continue
                if G.has_edge(u, v):
                    num_edges += 1
        num_edges = num_edges / 2
        coefficients[node] = (2 * num_edges) / (degree * (degree - 1))
    return coefficients


def avg_cc(coefficients: dict) -> float:
    avg = 0.0
    for value in coefficients.values():
        avg += value
    avg = avg / len(coefficients)
    return avg


if __name__ == "__main__":
    print("num_of_nodes:", num_of_nodes)
    print("num_of_edges:", num_of_edges)
    print("Average degree:", avg_degree)
    print("Density: ", get_density(G))
    print("Diameter: ", get_diameter(G))
    print("Avg Clustering Coefficient: ", avg_cc(clustering_coefficient(G)))

    # display graph using defaults
    nx.draw(G)
    plt.show()
