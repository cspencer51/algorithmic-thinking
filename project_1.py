"""
Functions for Algorithmic Thinking Project 1
"""

EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}

def make_complete_graph(num_nodes):
    """
    Takes a number of nodes and returns a dictionary corresponding to a
    complete directed graph with the specified number of nodes.
    """
    if num_nodes > 0:
        graph = {}

        for node in range(num_nodes):
            adj_nodes = range(num_nodes)
            adj_nodes.remove(node)

            graph[node] = set(adj_nodes)

        return graph
    else:
        return {}


def compute_in_degrees(digraph):
    """
    Takes a directed graph and computes the in-degrees for the nodes in the
    graph.
    """
    all_edges = []
    in_degrees = {}

    for edges in digraph.itervalues():
        all_edges += edges

    for virtex in digraph.iterkeys():
        in_degrees[virtex] = all_edges.count(virtex)

    return in_degrees

def in_degree_distribution(digraph):
    """
    Takes a directed graph and computes the unnormalized distribution of the
    in-degress of the graph.
    """
    in_degrees = compute_in_degrees(digraph)

    degree_dist = {}

    for degree in in_degrees.itervalues():
        if not degree in degree_dist:
            degree_dist[degree] = 1
        else:
            degree_dist[degree] += 1

    return degree_dist
    