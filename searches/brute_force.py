import itertools
from utils import solutionValue

def brute_force_search(graph):
    nodes = list(graph.nodes)
    adj = graph.adj
    nodes.sort()
    permutations = itertools.permutations(nodes)
    best_c = 0
    best_s = []
    for permutation in permutations:
        print(permutation)
        curr_s, curr_c = solutionValue(permutation,adj)
        if curr_c > best_c:
            best_c = curr_c
            best_s = curr_s
    return best_s, best_c
