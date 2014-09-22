"""
Functions for Algorithmic Thinking Project 2
"""

from collections import deque

EX_GRAPH = {0: set([1, 3, 4]),
            1: set([0, 2]),
            2: set([1, 3]),
            3: set([0, 2, 6]),
            4: set([0, 5]),
            5: set([4]),
            6: set([3, 7, 8]),
            7: set([6]),
            8: set([6]),
            9: set([10, 11]),
            10: set([9]),
            11: set([9])}

def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node and returns the
    set consisting of all nodes that are visited by a breadth-first search that
    starts at start_node.
    """
    queue = deque()

    #Initialize to infinity
    node_distance = {x: float('inf') for x in ugraph.iterkeys()}

    node_distance[start_node] = 0

    queue.append(start_node)

    while queue:
        node = queue.popleft()

        for neighbor in ugraph[node]:
            if node_distance[neighbor] == float('inf'):
                node_distance[neighbor] = node_distance[node] + 1

                queue.append(neighbor)

    visited = set()

    for node, distance in node_distance.iteritems():
        if distance != float('inf'):
            visited.add(node)

    return visited

def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph and returns a list of sets, where each set
    consists of all the nodes (and nothing else) in a connected component, and
    there is exactly one set in the list for each connected component in ugraph
    and nothing else.
    """
    connected_components = []
    unvisited_nodes = ugraph.keys()

    while unvisited_nodes:
        subgraph = bfs_visited(ugraph, unvisited_nodes[0])

        nodes = set()

        for key in subgraph:
            nodes.add(key)
            unvisited_nodes.remove(key)

        connected_components.append(nodes)

    return connected_components

def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer) of the
    largest connected component in ugraph.
    """
    connected_components = cc_visited(ugraph)

    return max(len(component) for component in connected_components)

def remove_node(ugraph, node_to_delete):
    """
    Removes node_to_delete and all its edges from the undirected graph ugraph
    and returns the resulting graph.
    """
    for edges in ugraph.itervalues():
        if node_to_delete in edges:
            edges.remove(node_to_delete)

    if node_to_delete in ugraph:
        del ugraph[node_to_delete]

    return ugraph

def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order and iterates
    through the nodes in attack_order. For each node in the list, the function
    removes the given node and its edges from the graph and then computes the
    size of the largest connected component for the resulting graph.

    The function should return a list whose k+1th entry is the size of the
    largest connected component in the graph after the removal of the first k
    nodes in attack_order. The first entry (indexed by zero) is the size of the
    largest connected component in the original graph.
    """
    my_graph = ugraph

    graph_sizes = [largest_cc_size(my_graph)]

    for node in attack_order:
        my_graph = remove_node(ugraph, node)
        if my_graph != {}:
            graph_sizes.append(largest_cc_size(my_graph))
        else:
            graph_sizes.append(0)

    return graph_sizes
