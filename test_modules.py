import pandas as pd
import numpy as np
import random

PRODUCTS = pd.DataFrame({
    'Names' : ["Dubalin", "Chocolate", "Sabritas", "Gansitos", "Bubaloo", "Panditas", "Kranky"],
    'Weight' : [.6, 1, .1, .6, .4, .2, .3],
    'Buy_Price': [60, 30, 80, 66, 34, 76, 33],
    'Sale_Price' : [70, 80, 140, 100, 320, 43, 124]
    })

def init_population(n):
    """Return a population of n random solutions. Each solution is 
    a 4x3 list, with each element being a selection of 3 distinct
    random barrels.
    """
    new_population = np.random.randint(low=1, high=6, size=(n, 7))
    print(new_population)
    #new_population_df = pd.DataFrame({'Quantity' : new_population})
    return new_population

def fitness(candidate):
    """Return number of unique outcomes. Iterate through all
    possible pairs of poisonous barrels and the twelve slots.
    For each poisonous pair generate the outcome as a list
    e.g. [0,1,2,3], where the indexes are the orchids and
    numbers they day that orchid died (3 indicates that it
    did not die). Calculate the number of unique outcomes by
    adding outcomes o a set and return 66 - the length of
    that set. For a perfect solution there are 66 unique
    outcomes, thus return 0.
    """
    result_weight = (PRODUCTS['Weight'] * candidate).sum()
    result_buy = (PRODUCTS['Buy_Price'] * candidate).sum()
    result_sale = (PRODUCTS['Sale_Price'] * candidate).sum()
    print(result_weight, result_buy, result_sale)
    if result_weight > 20:
        return 0
    if result_buy > 1000:
        return 0
    return result_sale - result_buy
def evaluation(population):
    """Return a population sorted by fitness."""
    return sorted(population, key= lambda x:fitness(x))

pop = init_population(10)
print(PRODUCTS)
print(pop[0])
score = fitness(pop[0])
print(score)
print(evaluation(pop))
