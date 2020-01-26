import networkx as nx
import numpy as np
import time
from utils import create_graph, draw_graph, solutionValue
import searches.annealing as an
import searches.brute_force as bf
import searches.halldorsson as hal
import searches.genetic as gen
import matplotlib.pyplot as plt
# graph = nx.Graph()
# graph.add_nodes_from([6, 8, 7, 3, 5, 2, 1, 9, 4])
# graph.add_edges_from([(6,8), (6,7), (8,2), (8,4), (7,3), (7,9), (3,5), (3,2), (3,1), (3,9)])
# graph = create_graph(nodes = 50, edges= 50)
# adj = graph.adj
# res = list(graph.nodes)
# solution, n = solutionValue(res,adj)
# print(n)
# print(solution)
# start = time.time()
# sol, c = bf.brute_force_search(graph)
# end = time.time()
# print('solution: {}\ncard: {}\n time:{}s'.format(sol, c, end - start))
# start1 = time.time()
# solution, card = an.simulated_annealing_search(graph)
# end1 = time.time()
# print('solution1: {}\ncard: {}\n time:{}s'.format(solution, card, end1 - start1))
# start2 = time.time()
# card2 = gen.genetic_search(graph)
# end2 = time.time()
# print('card: {}\n time:{}s'.format( card2, end2 - start2))
# draw_graph(graph)


def test(search_f, edges=10, nodes=10, draw=True):
    print('Creating graph')
    graph = create_graph(edges, nodes)

    print('Testing', search_f.__name__)
    start = time.time()
    result = search_f(graph)
    end = time.time()
    print('{} with {} nodes and {} edges took {:.3f}s'.format(search_f.__name__, nodes, edges, end - start))
    print('Final result', result)

    if draw:
        draw_graph(graph, result[0])


def compare(f1, f2, edges=10, nodes=10, iterations=100):
    print('Comparing {} and {}'.format(f1.__name__, f2.__name__))
    results = {
        f1.__name__: 0,
        f2.__name__: 0,
        'equal': 0
    }
    for i in range(0, iterations):
        print(i)
        graph = create_graph(edges, nodes)
        res_1 = f1(graph)[1]
        res_2 = f2(graph)[1]

        if res_1 > res_2:
            results[f1.__name__] += 1
        elif res_2 > res_1:
            results[f2.__name__] += 1
        else:
            results['equal'] += 1
    print(results)


def avg_results(functions, edges=10, nodes=10, iterations=10):
    results = {}
    sums = {}
    for f in functions:
        results[f.__name__] = []
        sums[f.__name__] = 0
    for i in range(0,iterations):
        print(i)
        graph = create_graph(edges, nodes)
        for f in functions:
            res = f(graph)[1]
            results[f.__name__].append(res)
            sums[f.__name__] += res
    plt.figure(figsize=(8, 6))
    ax = plt.subplot(111)
    averages = []
    _averages = {}
    for search_f in functions:
        name = search_f.__name__
        averages.append(sums[name] / iterations)
        print(name, averages[-1])
        _averages[name] = averages[-1]
        plt.bar([name], averages[-1])

    plt.grid(True, which='both', axis='y', zorder=0, alpha=1)
    plt.grid(which='minor', alpha=.3)
    major_ticks = np.arange(0, max(averages) + 1, 5)
    minor_ticks = np.arange(0, max(averages) + 1, 1)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)
    plt.legend(list(map(lambda f: f.__name__ + ' ' + str(_averages[f.__name__]), functions)), loc='upper center', bbox_to_anchor=(0.5, 0))
    plt.tick_params(axis='x', bottom=False, labelbottom=False)
    plt.title('Average for {} nodes and {} edges in {} iterations\n'.format(nodes, edges, iterations))
    plt.show()



def plot_results(function, edges= 10, nodes= 10, iterations = 100):
    results = []
    # graph = create_graph(edges, nodes)
    for i in range(0,iterations):
        print(i)
        # graph = create_graph(edges, nodes)
        results.append(function(graph)[1])

    plt.figure(figsize=(12, 6))
    ax = plt.subplot(111)
    ax.plot(range(1,iterations + 1), results)
    plt.grid(True, which='both', axis='y', zorder=0, alpha=1)
    major_ticks = np.arange(min(results)-1, max(results)+1, 1)
    ax.set_yticks(major_ticks)
    ax.set_label(function.__name__)
    plt.title("{} : {} nodes / {} edges".format(function.__name__, nodes, edges))
    plt.show()


def plot_results_by_iter(function, edges= 10, nodes= 10, iterations = 100):
    results = []
    graph = create_graph(edges, nodes)
    for i in range(0,iterations):
        print(i)
        results.append(function(graph, iterations = i)[1])

    plt.figure(figsize=(12, 6))
    ax = plt.subplot(111)
    ax.plot(range(1,iterations + 1), results)
    plt.grid(True, which='both', axis='y', zorder=0, alpha=1)
    major_ticks = np.arange(min(results)-1, max(results)+1, 1)
    ax.set_yticks(major_ticks)
    ax.set_label(function.__name__)
    plt.title("{} - Results by iterations \n{} nodes / {} edges".format(function.__name__, nodes, edges))

    plt.show()
