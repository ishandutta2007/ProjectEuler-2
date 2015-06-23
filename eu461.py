# ----------------------------------------------------------------- Almost Pi ----------------------------------------------------------------- #
#                                                                                                                                               #
#       Let f,n(k) = e^k/n - 1, for all non-negative integers k.                                                                                #
#                                                                                                                                               #
#       Remarkably, f,200(6) + f,200(75) + f,200(89) + f,200(226) = 3.141592644529… ≈ π.                                                        #
#                                                                                                                                               #
#       In fact, it is the best approximation of π of the form f,n(a) + f,n(b) + f,n(c) + f,n(d) for n = 200.                                   #
#                                                                                                                                               #
#       Let g(n) = a^2 + b^2 + c^2 + d^2 for a, b, c, d that minimize the error: |f,n(a) + f,n(b) + f,n(c) + f,n(d) - π|                        #
#       (where |x| denotes the absolute value of x).                                                                                            #
#                                                                                                                                               #
#       You are given g(200) = 6^2 + 75^2 + 89^2 + 226^2 = 64658.                                                                               #
#                                                                                                                                               #
#       Find g(10000).                                                                                                                          #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import math
import random

def f(n, k):
    return math.exp(k / n) - 1

def individual(length, min, max):
    'Create a member of the population.'
    return [random.randint(min, max) for x in range(length)]

def population(count, length, min, max):
    """
    Create a number of individuals (i.e. a population).

    count: the number of individuals in the population
    length: the number of values per individual
    min: the minimum possible value in an individual's list of values
    max: the maximum possible value in an individual's list of values

    """
    return [individual(length, min, max) for x in range(count)]

def fitness(individual, target):
    def get_best_last_element(a, b, c):
        s = math.pi - f(eu461.BASE, a) - f(eu461.BASE, b) - f(eu461.BASE, c)
        s += 1

        if s > 1:
            return round(math.log(s) * eu461.BASE)
        else:
            return 0

    def getg():
        return get_best_last_element
    """
    Determine the fitness of an individual. Higher is better.

    individual: the individual to evaluate
    target: the target number individuals are aiming for
    """
    l = get_best_last_element(individual[0], individual[1], individual[2])
    
    return abs(target - sum([f(eu461.BASE, k) for k in individual]) - f(eu461.BASE, l))

def grade(pop, target):
    'Find average fitness for a population.'
    return sum([fitness(x, target) for x in pop]) / (len(pop))

def evolve(pop, target, retain=0.1, random_select=0.5, mutate=0.3):
    graded = [(fitness(x, target), x) for x in pop]
    graded = [x[1] for x in sorted(graded)]
    
    retain_length = int(len(graded) * retain)
    parents = graded[:retain_length]
    
    # randomly add other individuals to
    # promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random.random():
            parents.append(individual)
            
    # mutate some individuals
    for individual in parents:
        if mutate > random.random():
            pos_to_mutate = random.randint(0, len(individual) - 1)
            
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = random.randint(min(individual), max(individual))
            
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = random.randint(0, parents_length - 1)
        female = random.randint(0, parents_length - 1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) // 2
            if random.randint(0, 1):
                child = male[:half] + female[half:]
            else:
                child = female[:half] + male[half:]
            children.append(child)
    parents.extend(children)
    
    return parents

def get_best_last_element(a, b, c):
    s = math.pi - f(eu461.BASE, a) - f(eu461.BASE, b) - f(eu461.BASE, c)
    s += 1
    
    if s > 0:
        return round(math.log(s) * eu461.BASE)
    else:
        return 0
    
def eu461():
    target = math.pi
    p_count = 1000
    i_length = 3
    i_min = 0
    i_max = round(eu461.BASE * math.log(math.pi + 1))

    p = population(p_count, i_length, i_min, i_max)
    fitness_history = [grade(p, target),]
    
    for i in range(150):
        p = evolve(p, target)
        fitness_history.append(grade(p, target))

    for datum in fitness_history:
        pass #print (datum)

    return p[0], get_best_last_element(p[0][0], p[0][1], p[0][2]), sum([f(eu461.BASE, k) for k in p[0]]) + f(eu461.BASE, get_best_last_element(p[0][0], p[0][1], p[0][2]))
eu461.BASE = 200

if __name__ == "__main__":
    startTime = time.clock()
    print (eu461())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")


