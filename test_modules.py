from itertools import combinations
import random

def init_population(n):
    """Return a population of n random solutions. Each solution is 
    a 4x3 list, with each element being a selection of 3 distinct
    random barrels.
    """
    print([random.sample(range(1, 6), 5) for i in range(n)])
    return ([random.sample(range(1, 6), 5) for i in range(n)])

init_population(10)