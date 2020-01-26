import random
import math
from utils import solutionValue

#kaze halldorsson n/log(n) skupova sa po log(n) elemenata
#medjutim ovo ne funkcionise (osim ako ja nisam nesto pogresio)
#probacu neki drugaciji pristup
#vise elemenata

def halldorsson(graph):
    best = list(graph.nodes)
    n = len(best)
    num_of_elements = math.ceil(math.log(n))
    print(math.log(n))
    adj = graph.adj
    print(n)
    subsets = math.ceil(n/math.log(n))
    best_c = 0
    best_s = []
    subset = []
    for _ in range(0,subsets):
        subset = random.sample(best, num_of_elements)
        print(subset)
        curr_s, curr_c = solutionValue(subset, adj)
        if curr_c > best_c:
            best_c = curr_c
            best_s = curr_s
    return best_s, best_c