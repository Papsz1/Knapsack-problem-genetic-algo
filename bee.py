import random

def input_from_file():
    f = open("input1.txt")
    knapsack_weight = int(f.readline())
    weights = f.readline()
    values = f.readline()
    weights = list(map(int, weights.split()))
    values = list(map(int, values.split()))
    weights = list(map(int, weights))
    f.close()
    return knapsack_weight, weights, values, len(weights)

# we store individuals (knapsack solution) in a list
# which is the same size as the number of items
# every item has a corresponding index, which is set to 1 
# if there is such an item in our solution, else we set it to 0
# For example for 4 items: 1 0 0 1

def initialise_population(n):
    init_nr_individuals = 8
    individuals = []
    for i in range (0, init_nr_individuals):
        individual = []
        for j in range (0,n):
            individual.append(random.randint(0,1))
        individual = list(map(bool, individual))
        individuals.append(individual)
    return individuals

# we randomly generate a new individual
def individual_generator():
    individual = []
    for j in range (0,n):
            individual.append(random.randint(0,1))
    individual = list(map(bool, individual))
    return individual

# the fitness will be the value of the items from the solution
# if their weight is not higher than the max

def fitness(individual): 
    individual_weight = 0; individual_value = 0
    for i in range(0,n):
        if (individual[i] == 1):
            individual_weight = individual_weight + weights[i]    
    
    if (individual_weight > knapsack_weight):
        return 0

    for i in range(0,n):
        if (individual[i] == 1):
            individual_value = individual_value + values[i]    

    return individual_value

# we determine the probability of each solution to be chosen

def prob_value(individual):
    fitness_value = 0
    for i in individuals:
        fitness_value = fitness_value + fitness(i)
    if (fitness_value != 0):
        prob_v = fitness(individual) / fitness_value
    else:
        return 0
    return prob_v

def population_examination(changes):
    global individuals

    for i in range(0, len(individuals)):
        v = [0] * n
        for j in range(0, n):
            r_individual = individual_generator()
            sz_individual = random.randint(0, len(individuals)-1)
            v[j] = individuals[i][j] ^ (r_individual[j] & (individuals[i][j] ^ individuals[sz_individual][j])) # keplet alapjan
        if (fitness(v) > fitness(individuals[i])):
            individuals[i] = v
            changes[i] = 1

    prob_values = []

    for i in individuals:
        prob_values.append(prob_value(i))
    
    onlookers = []
    for i in range (0, len(individuals)):
        if (random.uniform(0, 1) > prob_values[i]):
            onlookers.append(i)

    for i in onlookers:
        v = [0] * n
        for j in range(0, n):
            r_individual = individual_generator()
            sz_individual = random.randint(0, len(individuals)-1)
            v[j] = individuals[i][j] ^ (r_individual[j] & (individuals[i][j] ^ individuals[sz_individual][j]))
        if (fitness(v) > fitness(individuals[i])):
            individuals[i] = v
            changes[i] = 1

def population_generator():
    changes = [0] * len(individuals)
    for i in range(0,100):
        population_examination(changes)
        if (i % 10 == 0):
            for i in range (0, len(individuals)):
                if (changes[i] == 0):
                    individuals[i] = individual_generator()

    max_value = -1
    max_solution = []
    for i in individuals:
        fitness_individual = fitness(i)
        if (fitness(i) > max_value):
            max_value = fitness_individual
            max_solution = i

    best_solution = list(map(int,max_solution))
    best_fitness = fitness(max_solution)
    return best_solution, best_fitness


def main():
    global knapsack_weight, weights, values, n, individuals
    knapsack_weight, weights, values, n = input_from_file()
    individuals = initialise_population(n)
    best_solution, best_fitness = population_generator()
    return best_solution, best_fitness

main()