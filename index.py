from testing import *
import searches.annealing as an
import searches.brute_force as bf
import searches.halldorsson as hal
import searches.genetic as gen


# test(hal.halldorsson, nodes = 100, edges = 100, draw= False)
# test(an.simulated_annealing_search, nodes=100, edges= 100, draw=False)

# compare(an.simulated_annealing_search, gen.genetic_search)

# avg_results([an.simulated_annealing_search,hal.halldorsson], nodes = 50, edges=50)
plot_results_by_iter(an.simulated_annealing_search,edges= 50, nodes=50, iterations=500)