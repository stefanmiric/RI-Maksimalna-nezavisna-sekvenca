import random
import math
from utils import solutionValue


#moguca popravka, nekako drugacije birati okolinu, po nekoj heuristici

def simulated_annealing_search(graph, iterations = 1000):
    best = list(graph.nodes)
    #bolje uzeti cvor sa manjim stepenom na pocetku zato sto je veca sansa da nece moci u niz na kraju 
    # best.sort(key=lambda x: graph.degree[x])
    best_s, best_c = solutionValue(best, graph.adj)
    for i in range(1,iterations):
        current = best
        a = random.randint(0, len(best) - 1)
        b = random.randint(0, len(best) - 1)
        current[a], current[b] = current[b], current[a]
        current_s, current_c = solutionValue(current,graph.adj)
        if (current_c > best_c) or (1 / i > random.random()):
            best = current
            best_c = current_c
            best_s = current_s
    return best_s, best_c

def simulated_annealing_search_slow(graph, iterations = 1000):
    best = list(graph.nodes)
    #bolje uzeti cvor sa manjim stepenom na pocetku zato sto je veca sansa da nece moci u niz na kraju 
    # best.sort(key=lambda x: graph.degree[x])
    best_s, best_c = solutionValue(best, graph.adj)
    for i in range(1,iterations):
        current = best
        a = random.randint(0, len(best) - 1)
        b = random.randint(0, len(best) - 1)
        current[a], current[b] = current[b], current[a]
        current_s, current_c = solutionValue(current,graph.adj)
        if (current_c > best_c) or (1 / math.sqrt(i) > random.random()):
            best = current
            best_c = current_c
            best_s = current_s
    return best_s, best_c
