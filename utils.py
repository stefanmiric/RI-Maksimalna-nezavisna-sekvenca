import networkx as nx
import matplotlib.pyplot as plt
import random


def create_graph(edges = 10, nodes = 10):
    if nodes <= 1:
        raise Exception('2 or more nodes required')

    graph = nx.Graph()
    while len(graph.edges < edges):
        node_a = random.randint(1,nodes)
        node_b = random.randint(1,nodes)
        while node_a == node_b:
            node_b = random.randint(1,nodes)
        if node_a > node_b:
            node_a, node_b = node_b, node_a
        if (node_a,node_b) in graph.edges:
            continue
        graph.add_edge(node_a,node_b)
    
    return graph


def draw_graph(graph):
    plt.figure(figsize=(8, 8))
    nx.draw(graph, with_labels=False)
    plt.show()
