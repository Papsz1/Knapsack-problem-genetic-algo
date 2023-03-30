import bee
import genetic
import matplotlib.pyplot as plt
import time

def main():
    n = 1000 # number of iterations the tests will be run
    fig, ax = plt.subplots(1, 2)

    start = time.time()
    average_bee_fitness = 0
    bee_fitnesses = []
    for i in range(0, n):
        best_solution, best_fitness = bee.main()
        average_bee_fitness = average_bee_fitness + best_fitness
        bee_fitnesses.append(best_fitness)

    end = time.time()
    bee_time = end-start

    ax[0].plot(bee_fitnesses)
    ax[0].title.set_text("Artificial Bee Colony algorithm")
    ax[0].set_ylim([0, 1500])

    start = time.time()
    average_genetic_fitness = 0
    genetic_fitnesses = []
    for i in range(0, n):
        best_solution, best_fitness = genetic.main()
        average_genetic_fitness = average_genetic_fitness + best_fitness
        genetic_fitnesses.append(best_fitness)
    end = time.time()

    ax[1].plot(genetic_fitnesses)
    ax[1].title.set_text("Genetic algorithm")
    ax[1].set_ylim([0, 1500])


    genetic_time = end-start
    print("Average bee fitness:", average_bee_fitness/n)
    print("Required time:", bee_time, "s")

    print("Average genetic fitness:", average_genetic_fitness/n)
    print("Required time:", genetic_time, "s")

    plt.show()
    

main()