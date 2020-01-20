import networkx as nx
import time
from utils import create_graph, draw_graph, solutionValue
import searches.annealing as an
import searches.brute_force as bf

# graph = nx.Graph()
# graph.add_nodes_from([6, 8, 7, 3, 5, 2, 1, 9, 4])
# graph.add_edges_from([(6,8), (6,7), (8,2), (8,4), (7,3), (7,9), (3,5), (3,2), (3,1), (3,9)])

graph = create_graph(nodes = 50, edges= 50)

# adj = graph.adj
# res = list(graph.nodes)

# solution, n = solutionValue(res,adj)

# print(n)
# print(solution)
start1 = time.time()

solution, card = an.simulated_annealing_search(graph)
end1 = time.time()

# start2 = time.time()
# bf.brute_force_search(graph)
# end2 = time.time()

print('solution1: {}\ncard: {}\n time:{}s'.format(solution, card, end1 - start1))
# print('solution2: {}\ncard: {}\n time:{}s'.format(solution, card, end2 - start2))

draw_graph(graph)
