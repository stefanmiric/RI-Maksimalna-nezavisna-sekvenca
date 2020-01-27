from testing import *
import searches.annealing as an
import searches.brute_force as bf
import searches.halldorsson as hal
import searches.genetic as gen


# test(hal.halldorsson, nodes = 100, edges = 100, draw= False)
# test(an.simulated_annealing_search, nodes=100, edges= 100, draw=False)

# compare(an.simulated_annealing_search_sort, gen.genetic_search ,edges=50,nodes=50)

avg_results([an.simulated_annealing_search,an.simulated_annealing_search_slow, an.simulated_annealing_search_sort, gen.genetic_search], nodes = 200, edges=300, iterations= 100)
# plot_results_by_iter(gen.genetic_search,edges= 50, nodes=50, iterations=100)

# test(an.simulated_annealing_search,nodes=50,edges=50)
# plot_results(gen.genetic_search,nodes=50,edges=50)
# test(gen.genetic_search, 50, 50)

# avg_results([an.simulated_annealing_search, gen.genetic_search], 50, 50, 100)
# test(bf.brute_force_search)

# 1. {'simulated_annealing_search': 1, 'genetic_search': 84, 'equal': 15} 50 50 100
# 2. {'simulated_annealing_search': 38, 'simulated_annealing_search_sort': 31, 'equal': 31} 50 50 100
# 3. {'simulated_annealing_search_sort': 6, 'genetic_search': 86, 'equal': 8}


#bf 
#8 = 3.386s
#9 = 35.196s
#10 = 429.022s ~ 7min
#11 > 2.5 sata

# plot_results_by_iter(an.simulated_annealing_search,edges=50,nodes=50, iterations = 600)