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



def init_population(n):
    """Return a population of n random solutions. Each solution is 
    a 4x3 list, with each element being a selection of 3 distinct
    random barrels.
    """
    global n_product
    new_population = np.random.randint(low=min_value, high=max_value, size=(5, 10))
    return new_population

def random_value(n):
    if random.random() < p_mutate: 
        o = random.randrange(1, 8)    
        with open('results1.txt', 'a') as f:
            f.write('Value to change: \n')
            f.write(str(n) + '\n')
            f.write('New: \n')
            f.write(str(o) + '\n')
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
    with open('results1.txt', 'a') as f:
        f.write('Previous: \n')
        f.write(str(population) + '\n')
        f.write('New: \n')
        f.write(str(mutated_population) + '\n')
    return mutated_population


n_pop = 2
n_generations = 10
p_mutate = 1
with open('results1.txt', 'a') as f:
    f.write("================== \n")
    f.write("population size: {0} \n generations: {1} \n mutation %: {2} \n". format(n_pop, n_generations, p_mutate))
for k in range(10):
    pop = init_population(2)
    mutation(pop)


