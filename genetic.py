import random

def beolvasas():
    f = open("input1.txt")
    knapsack_weight = int(f.readline())
    weights = f.readline()
    values = f.readline()
    weights = list(map(int, weights.split()))
    values = list(map(int, values.split()))
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
        individuals.append(individual)
    return individuals

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

# the selection is tournament-based, we randomly choose 4 individuals
# and play a tournament between them based on their fitness, selecting the two winners

def selection():
    parent_index = random.sample(range(0,len(individuals)), 4)
    parents = []
    parents.append(individuals[parent_index[0]] if fitness(individuals[parent_index[0]]) > fitness(individuals[parent_index[1]]) else individuals[parent_index[1]])
    parents.append(individuals[parent_index[2]] if fitness(individuals[parent_index[2]]) > fitness(individuals[parent_index[3]]) else individuals[parent_index[3]])
    return parents

# the crossover used is single-point, we cut the list at its halfway point
# and switch them up

def crossover(parents):
    children = []
    halfpoint = int(n/2)
    child1 = parents[0][:halfpoint] + parents[1][halfpoint:]
    child2 = parents[1][:halfpoint] + parents[0][halfpoint:]

    children.append(child1); children.append(child2)

    return children

# the mutation will be the random removal or adding of an item to the knapsack

def mutation(individual):
    item = random.randint(0,n-1)
    individual[item] = 1 if individual[item] == 0 else 0
    return individual

def create_population():
    new_population = []
    reprod_coeff = 29
    mutation_coeff = 1
    crossover_coeff = 47
    children = []

    while (len(new_population) < n):
        parents = selection()

        if random.randint(1,100) < reprod_coeff:
            children = parents
        else:
            if random.randint(1,100) < crossover_coeff:
                children = crossover(parents)
            
            if random.randint(1,100) < mutation_coeff and len(children) != 0:
                children[0] = mutation(children[0])
                children[1] = mutation(children[1])
        
        if (len(children) != 0):
            new_population.append(children[0])
            new_population.append(children[1])

    return new_population

def population_generator():
    global individuals

    for i in range (0,100):
        individuals = create_population()
    
    max_value = -1
    max_solution = []
    for i in individuals:
        fitness_individual = fitness(i)
        if (fitness(i) > max_value):
            max_value = fitness_individual
            max_solution = i

    return max_solution, max_value

def main():
    global knapsack_weight, weights, values, n, individuals
    knapsack_weight, weights, values, n = beolvasas()
    individuals = initialise_population(n)
    
    best_solution, best_fitness = population_generator()
    return best_solution, best_fitness

main()