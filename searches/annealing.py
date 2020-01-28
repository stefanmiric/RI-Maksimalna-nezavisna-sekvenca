import random
import math
from utils import solutionValue


#moguca popravka, nekako drugacije birati okolinu, po nekoj heuristici

def simulated_annealing_search(graph, iterations = 500):
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

def simulated_annealing_search_slow(graph, iterations = 500):
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

def simulated_annealing_search_sort(graph, iterations = 500):
    best = list(graph.nodes)
    best.sort(key=lambda x: graph.degree[x])
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

def simulated_annealing_search_variation(graph, iterations = 500):
    #vise random izmena, ali moguce je zameniti n/2 cvorova
    best = list(graph.nodes)
    best_s, best_c = solutionValue(best, graph.adj)
    for i in range(1,iterations):
        current = best
        n = random.randint(0, math.floor((len(best) - 1)/2))
        indexes = []
        values = []
        for _ in range(n):
            r=random.randint(0, len(best) - 1)
            indexes.append(r)
            values.append(current[r])
        random.shuffle(indexes)
        random.shuffle(values)

        for j in range(n):
            index = indexes[j]
            current[index] = values[j]

        current_s, current_c = solutionValue(current,graph.adj)
        if (current_c > best_c) or (1 / i > random.random()):
            best = current
            best_c = current_c
            best_s = current_s
    return best_s, best_c


def simulated_annealing_search_variation1(graph, iterations = 500):
    #moguce je zameniti svih n cvorova
    best = list(graph.nodes)
    best_s, best_c = solutionValue(best, graph.adj)
    for i in range(1,iterations):
        current = best
        n = random.randint(0, (len(best) - 1))
        indexes = []
        values = []
        for _ in range(n):
            r=random.randint(0, len(best) - 1)
            indexes.append(r)
            values.append(current[r])
        random.shuffle(indexes)
        random.shuffle(values)

        for j in range(n):
            index = indexes[j]
            current[index] = values[j]

        current_s, current_c = solutionValue(current,graph.adj)
        if (current_c > best_c) or (1 / i > random.random()):
            best = current
            best_c = current_c
            best_s = current_s
    return best_s, best_c


def simulated_annealing_search_variation2(graph, iterations = 500):
    #zamena 3 cvora
    best = list(graph.nodes)
    best_s, best_c = solutionValue(best, graph.adj)
    for i in range(1,iterations):
        current = best
        n = 3
        indexes = []
        values = []
        for _ in range(n):
            r=random.randint(0, len(best) - 1)
            indexes.append(r)
            values.append(current[r])
        random.shuffle(indexes)
        random.shuffle(values)

        for j in range(n):
            index = indexes[j]
            current[index] = values[j]

        current_s, current_c = solutionValue(current,graph.adj)
        if (current_c > best_c) or (1 / i > random.random()):
            best = current
            best_c = current_c
            best_s = current_s
    return best_s, best_c
