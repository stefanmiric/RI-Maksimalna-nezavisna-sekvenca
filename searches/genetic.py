from utils import solutionValue
import math
import itertools
import numpy as np
import random


class GeneticAlgorithm:

    def __init__(self, graph):
        self._graph = graph
        self._nodes = graph.nodes

        self._iterations = 100
        self._generation_size = 100
        self._mutation_rate = 0.01
        self._current_iteration = 0
        self._chromosome_length = len(self._nodes)
        self._best_chromosome = Chromosome(None, 0)
        self._solution = []

    def optimize(self):
        chromosomes = self.initialize_population()
        new_gen = chromosomes
        while not self.stop_condition():
            chromosomes.sort(key=lambda chromo : chromo.fitness)
            for i in range(30):
                new_gen[i] = chromosomes[i]
            for i in range(30,100,2):
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
        max = 0
        k = -1
        for i in range(8):
            j = random.randrange(100)
            if population[j].fitness > max:
                max = population[j].fitness
                k = j
        return k

    def crossover(self, parent1, parent2):
        """order 1 crossover"""

        parent1_content = parent1.content
        parent2_content = parent2.content

        swath_size = random.randint(1, self._chromosome_length)
        swath_pos = random.randint(0, self._chromosome_length - swath_size)

        child1_content = parent1_content
        child2_content = parent2_content

        selected = [child1_content[i] for i in range(swath_pos, swath_pos + swath_size)]
        order = []
        for k in range(0, self._chromosome_length):
            if parent2_content[k] in selected:
                selected.remove(parent2_content[k])
            else:
                order.append(parent2_content[k])
        for i in range(self._chromosome_length):
            if swath_pos <= i < swath_pos + swath_size:
                continue
            next = order.pop(0)
            child1_content[i] = next



        selected = [child2_content[i] for i in range(swath_pos, swath_pos + swath_size)]
        order = []
        for k in range(0, self._chromosome_length):
            if parent1_content[k] in selected:
                selected.remove(parent1_content[k])
            else:
                order.append(parent1_content[k])
        for i in range(self._chromosome_length):
            if swath_pos <= i < swath_pos + swath_size:
                continue
            next = order.pop(0)
            child2_content[i] = next


        child1 = Chromosome(child1_content, self.fitness(child1_content))
        child2 = Chromosome(child2_content, self.fitness(child2_content))
        return (child1, child2)


    def fitness(self, permutation):
        sol, cardinality = solutionValue(permutation,self._graph.adj)
        if cardinality > self._best_chromosome.fitness:
            self._best_chromosome.fitness = cardinality
            self._best_chromosome.content = sol
            self._solution = sol
        return cardinality

    def initialize_population(self):
        init = []
        for i in range(self._generation_size):
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

def genetic_search(graph):
    return GeneticAlgorithm(graph).optimize()
