
import pandas as pd
import numpy as np
import random
import math

PRODUCTS = pd.DataFrame({
    'Names' : ["Dubalin", "Chocolate", "Sabritas", "Gansitos", "Bubaloo", "Panditas", "Kranky"],
    'Weight' : [.6, .5, .1, .6, 2, .2, .3],
    'Buy_Price': [60, 30, 80, 66, 34, 76, 33],
    'Sale_Price' : [70, 80, 140, 100, 170, 76, 124]
    })

n_product = len(PRODUCTS.index)
max_value = 7
min_value = 1


def init_population(n):
    """Return a population of n random solutions. Each solution is 
    a 4x3 list, with each element being a selection of 3 distinct
    random barrels.
    """
    global n_product
    new_population = np.random.randint(low=min_value, high=max_value, size=(n, n_product))
    return new_population

def fitness(candidate):
    """Give the score of the revenue obtain, and penalize the score when
    it doesn't comply with the restrictions (not 0 or negative numbers from the start)
    """
    weight_limit = 15
    buy_limit = 1000
    result_weight = (PRODUCTS['Weight'] * candidate).sum()
    result_buy = (PRODUCTS['Buy_Price'] * candidate).sum()
    result_sale = (PRODUCTS['Sale_Price'] * candidate).sum()
    score = result_sale - result_buy
    negative = 0
    if result_weight > weight_limit:
        negative = (weight_limit - result_weight)* (score / weight_limit)
    if result_buy > buy_limit:
        negative = negative + (buy_limit - result_buy) * (score / buy_limit)
    if result_weight > weight_limit or result_buy > buy_limit:
        return score + negative
    score = result_sale - result_buy
    return score

def evaluation(population):
    """Return a population sorted by fitness."""
    return sorted(population, key= lambda x:fitness(x), reverse= True)

def selection(population, percentage_selection):
    """Return an even amount of population, considering the selection %"""
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
    """
    Used to assign a random value to an element of the matrix.
    It considers the mutation % when deciding if the value changes the value or if  
    it stays the same.
    """
    if random.random() < p_mutate: 
        o = random.randrange(min_value, max_value + 1)
        return o
    return n

def mutation(population):
    """Return a mutated population (out-of-place). 
    It considers every element of the matrix using the random_value function
    """
    mutate = np.vectorize(random_value)
    mutated_population = mutate(population)
    return mutated_population


def is_solution(candidate):
    
    """Check if the combinations are complying with the restrictions.
    If not, it eliminates that combination from the final population.
    """
    weight_limit = 15
    buy_limit = 1000
    result_weight = (PRODUCTS['Weight'] * candidate).sum()
    result_buy = (PRODUCTS['Buy_Price'] * candidate).sum()
    if result_weight > weight_limit or result_buy > buy_limit:
        return False
    else: 
        return True

def gen_algorithm():
    """Is the whole genetic algorithm, using every step of it.
    It also considers a filter to eliminate non complying solution
    """
    pop = init_population(n_pop)
    ranking = evaluation(pop)
    best_score = 0
    for i in range(n_generations):
        parents = selection(ranking, per_selection)
        children = crossover(parents)
        children = mutation(children)
        new_pop = np.empty((n_pop, n_product), dtype=int)
        new_pop[:children.shape[0]] = children
        new_pop[children.shape[0]:] = pop[:(n_pop-children.shape[0])]
        pop = evaluation(new_pop)
        best_score = fitness(pop[0])
        with open('results_f.txt', 'a') as f:
            f.write(str(best_score) + '\n')
    r_sol = []
    for com in pop:
        is_sol = is_solution(com)
        if is_sol:
            r_sol.append(com)
    pop = np.array(r_sol)
    solution = evaluation(pop)[0]
    return solution




n_pop = 500
n_generations = 1000
p_mutate = 0.40
per_selection = 0.70
print("==================")
print("population size: {0} \n generations: {1} \n mutation %: {2} \n selection %: {3}". format(n_pop, n_generations, p_mutate, per_selection))
solution = gen_algorithm()
print(solution)
print(fitness(solution))