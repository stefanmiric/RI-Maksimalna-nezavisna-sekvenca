from utils import solutionValue
import math
import itertools
import numpy as np
import random


class GeneticAlgorithm:

    def __init__(self, graph, iter):
        self._graph = graph
        self._nodes = graph.nodes

        self._iterations = iter
        self._generation_size = 50
        self._mutation_rate = 0.01
        self._current_iteration = 0
        self._chromosome_length = len(self._nodes)
        self._best_chromosome = Chromosome(None, 0)
        self._solution = []

    def optimize(self):
        #no elites
        chromosomes = self.initialize_population()
        new_gen = chromosomes
        while not self.stop_condition():
            chromosomes.sort(key=lambda chromo : chromo.fitness)
            # for i in range(30):
            #     new_gen[i] = chromosomes[i]
            for i in range(0,self._generation_size,2):
                k1 = self.selection(chromosomes)
                k2 = self.selection(chromosomes)
                (child1, child2) = self.crossover(chromosomes[k1], chromosomes[k2])
                self.mutation(child1)
                self.mutation(child2)
                new_gen[i] = child1
                new_gen[i+1] = child2
            chromosomes = new_gen

            self._current_iteration += 1
            if self._current_iteration % 10 == 0:
                print("Iteration %d " % self._current_iteration)
                # print("Best chromosome: ", chromosomes)

        print("Best is ", self._solution)
        return self._best_chromosome.content, self._best_chromosome.fitness

    def mutation(self, chromosome):
        t = random.random()
        if t < self._mutation_rate:
            i = random.randint(0, self._chromosome_length - 1)
            j = random.randint(0, self._chromosome_length - 1)

            content = chromosome.content

            tmp = content[i]
            content[i] = content[j]
            content[j] = tmp

            chromosome.content = content
            chromosome.fitness = self.fitness(content)

        return chromosome


    def selection(self, population):
        # tournament selection
        max = 0
        k = -1
        for _ in range(8):
            j = random.randrange(self._generation_size)
            if population[j].fitness > max:
                max = population[j].fitness
                k = j
        return k


    def crossover(self, parent1, parent2):
        #order 1 crossover
        parent1_content = parent1.content
        parent2_content = parent2.content

        size = len(parent1_content)
        child1, child2 = [-1] * size, [-1] * size

        start, end = sorted([random.randrange(size) for _ in range(2)])

        child1_inherited = []
        child2_inherited = []
        for i in range(start, end + 1):
            child1[i] = parent1_content[i]
            child2[i] = parent2_content[i]
            child1_inherited.append(parent1_content[i])
            child2_inherited.append(parent2_content[i])
        currentp1 , currentp2 = 0, 0
        fixed_pos = list(range(start, end+1))
        i=0
        while i < size:
            if i in fixed_pos:
                i+=1
                continue
            test_c1 = child1[i]
            test_c2 = child2[i]
            if test_c1 == -1:
                p2_trait = parent2_content[currentp2]
                while p2_trait in child1_inherited:
                    currentp2 +=1
                    p2_trait = parent2_content[currentp2]
                child1[i] = p2_trait
                child1_inherited.append(p2_trait)

            if test_c2 == -1:
                p1_trait = parent1_content[currentp1]
                while p1_trait in child2_inherited:
                    currentp1 +=1
                    p1_trait = parent1_content[currentp1]
                child2[i] = p1_trait
                child2_inherited.append(p1_trait)

            i+=1
        return (Chromosome(child1, self.fitness(child1)), Chromosome(child2, self.fitness(child2))
)




    def fitness(self, permutation):
        sol, cardinality = solutionValue(permutation,self._graph.adj)
        if cardinality > self._best_chromosome.fitness:
            self._best_chromosome.fitness = cardinality
            self._best_chromosome.content = sol
            self._solution = sol
        return cardinality

    def initialize_population(self):
        init = []
        for _ in range(self._generation_size):
            ins = np.random.permutation(self._nodes).tolist()
            init.append(Chromosome(ins, self.fitness(ins)))
        return init

    def stop_condition(self):
        return self._current_iteration > self._iterations

class Chromosome:
    def __init__(self, content, fitness):
        self.content = content
        self.fitness = fitness

    def __str__(self):
        return f"{self.content}\n{self.fitness}"

    def __repr__(self):
        return f"{self.content}\n{self.fitness}"

def genetic_search(graph, iterations = 50):
    return GeneticAlgorithm(graph, iterations).optimize()
