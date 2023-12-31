import pandas as pd
import numpy as np
import random
import math
import time

PRODUCTS = pd.DataFrame({
    'Names' : ["Dubalin", "Chocolate", "Sabritas", "Gansitos", "Bubaloo", "Panditas", "Kranky"],
    'Weight' : [.6, .5, .1, .6, 2, .2, .3],
    'Buy_Price': [60, 30, 80, 66, 34, 76, 33],
    'Sale_Price' : [70, 80, 140, 100, 170, 76, 124]
    })

n_product = len(PRODUCTS.index)
max_value = 7
min_value = 1

n_pop = 200
n_generations = 1000
p_mutate = 0.90
per_selection = 0.50

def init_population(n):
    """Return a population of n random solutions. Each solution is 
    a 4x3 list, with each element being a selection of 3 distinct
    random barrels.
    """
    global n_product
    new_population = np.random.randint(low=min_value, high=max_value, size=(n, n_product))
    return new_population

def fitness(candidate):
    """Give the score of the 
    """
    result_weight = (PRODUCTS['Weight'] * candidate).sum()
    result_buy = (PRODUCTS['Buy_Price'] * candidate).sum()
    result_sale = (PRODUCTS['Sale_Price'] * candidate).sum()
    if result_weight > 15 or result_buy > 1000:
        return 0
    #if result_weight > 15:
    #    return (15 - result_weight) * 66.67
    #if result_buy > 1000:
    #    return 1500 - result_buy
    return result_sale - result_buy

def evaluation(population):
    """Return a population sorted by fitness."""
    return sorted(population, key= lambda x:fitness(x), reverse= True)

def selection(population, percentage_selection):
    """Return top half of population."""
    n_parents = math.ceil(len(population) * percentage_selection / 2) * 2
    n_parents = int(n_parents)
    return population[:n_parents]

def crossover(parents : np.array):
    """Return a new population, generated by pairing best solution with second best, and so forth. 
    """
    children = np.empty((len(parents), n_product), dtype=int)
    n_children = len(parents)
    for i in range(n_children): # Cross N times
        if i % 2 == 0:
            parent1, parent2 = parents[i], parents[i+1]
            child1 = np.empty(n_product)
            child2 = np.empty(n_product)
            child1[:int(n_product / 2)] = parent1[:int(n_product / 2)]
            child1[int(n_product / 2):] = parent2[int((n_product / 2)):]
            child2[:int(n_product / 2)] = parent2[:int(n_product / 2)]
            child2[int(n_product / 2):] = parent1[int(n_product / 2):]
            children[i] = child1
            children[i+1] = child2
    return children

def random_value(n):
    if random.random() < p_mutate: 
        o = random.randrange(1, 8)
        return o
    return n
    

def mutation(population):
    """Return a mutated population (out-of-place). For each
    candidate, mutate with probability p_mutate.
    If mutate:
        Select random slot.
        Select a randon integer to change the value excluding the preceding value.
    Else:
        The candidate is not affected.
    Return new (partially mutated) population.
    """
    mutate = np.vectorize(random_value)
    mutated_population = mutate(population)
    return mutated_population

def gen_algorithm():
    pop = init_population(n_pop)
    ranking = evaluation(pop)

    for i in range(n_generations):
        parents = selection(ranking, per_selection)
        children = crossover(parents)
        children = mutation(children)
        new_pop = np.empty((n_pop, n_product), dtype=int)
        new_pop[:children.shape[0]] = children
        new_pop[children.shape[0]:] = pop[:(n_pop-children.shape[0])]
        pop = evaluation(new_pop)
    solution = evaluation(pop)[0]
    return solution

print(PRODUCTS)


n_p = 50
n_g = 500
p_mutate = 0.1
per_selection = 0.50
for i in range(1, 21):
    n_pop = n_p * i
    for j in range(1, 3):
        n_generations = n_g * j
        with open('results_2.txt', 'a') as f:
            f.write("================== \n")
            f.write("population size: {0} \n generations: {1} \n mutation %: {2} \n selection %: {3} \n". format(n_pop, n_generations, p_mutate, per_selection))
        sol1 = []
        ran1 = []
        for k in range(10):
            st = time.time()
            solution = gen_algorithm()
            et = time.time()
            elapsed_time = et - st
            with open('results_2.txt', 'a') as f:
                f.write('Execution time: ' + str(elapsed_time) + ' seconds\n')
            sol1.append(solution)
            ran1.append(fitness(solution))
        with open('results_2.txt', 'a') as f:
            f.write("Ganancias \n")
            for score in ran1:
                f.write(str(score) + "\n")
            f.write("Mejor Solución \n")
            f.write(str(sol1[ran1.index(max(ran1))]) + "\n")
            f.write("Max Ganancia \n")
            f.write(str(max(ran1)) + "\n")

n_pop = 500
n_generations = 1000
p_m = 0.1
p_s = 0.1
for i in range(1, 11):
    p_mutate = p_m * i
    for j in range(1, 11):
        if i == 1 and j == 1:
            break
        per_selection = p_s * j
        with open('results.txt', 'a') as f:
            f.write("================== \n")
            f.write("population size: {0} \n generations: {1} \n mutation %: {2} \n selection %: {3} \n". format(n_pop, n_generations, p_mutate, per_selection))
        sol1 = []
        ran1 = []
        for k in range(10):
            st = time.time()
            solution = gen_algorithm()
            et = time.time()
            elapsed_time = et - st
            with open('results.txt', 'a') as f:
                f.write('Execution time: ' + str(elapsed_time) + ' seconds\n')
            sol1.append(solution)
            ran1.append(fitness(solution))
        with open('results.txt', 'a') as f:
            f.write("Ganancias \n")
            for score in ran1:
                f.write(str(score) + "\n")
            f.write("Mejor Solución \n")
            f.write(str(sol1[ran1.index(max(ran1))]) + "\n")
            f.write("Max Ganancia \n")
            f.write(str(max(ran1)) + "\n")
