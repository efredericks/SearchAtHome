# string-search.py
# Erik Fredericks, 2020
# Executes a string search optimization using a GA

#####
import sys
import random
import multiprocessing as mpc  # Used for testing/comparison purposes

#### EXAMPLES
from helloevolve import StringGA
####

### ---------------------------------------------------------------------------
# Generate random configs

if __name__ == "__main__":
    # Accept a seed value from the controller
    if len(sys.argv) > 1:
      print("Running seed {0}".format(sys.argv[1]))
      seed = sys.argv[1]
    else:
      print("Running default seed 1")
      seed = 1

    ga = StringGA(pop_size=500, generations=500000, optimal="12th Symposium for Search-Based Software Engineering | http://ssbse2020.di.uniba.it/", seed=seed)
    pool = mpc.Pool(mpc.cpu_count()-1)

    population = ga.random_population()
    done = False
    winner = ""
    total_gens = 0
    for generation in range(ga.GENERATIONS):

      print("Generation %s... Random sample: '%s'" % (generation, population[0]))
      weighted_population = []

      # Add individuals and their respective fitness levels to the weighted
      # population list. This will be used to pull out individuals via certain
      # probabilities during the selection phase. Then, reset the population list
      # so we can repopulate it after selection.

      # MPC version - commented to get sequential values
      #fitness_vals = pool.map(ga.fitness, population)
      #for i in range(len(population)):
      #    if fitness_vals[i] == 0:
      #        pair = (population[i], 1.0)
      #    else:
      #        pair = (population[i], 1.0/fitness_vals[i])
      #    weighted_population.append(pair)

      #   if population[i] == ga.OPTIMAL:
      #       winner = population[i]#individual
      #       total_gens = generation
      #       done = True
      
      # Loop through population and evaluate
      for individual in population:
        fitness_val = ga.fitness(individual)

        # Generate the (individual,fitness) pair, taking in account whether or
        # not we will accidently divide by zero.
        if fitness_val == 0:
          pair = (individual, 1.0)
        else:
          pair = (individual, 1.0/fitness_val)

        weighted_population.append(pair)

        if (individual == ga.OPTIMAL):
            winner = individual
            done = True

      if done:
          print("Found the answer early at Generation {0}! [{1}]".format(generation,winner))
          break

      population = []

      # Select two random individuals, based on their fitness probabilites, cross
      # their genes over at a random point, mutate them, and add them back to the
      # population for the next iteration.
      for _ in range(int(ga.POP_SIZE/2)):
        # Selection
        ind1 = ga.weighted_choice(weighted_population)
        ind2 = ga.weighted_choice(weighted_population)

        # Crossover
        ind1, ind2 = ga.crossover(ind1, ind2)

        # Mutate and add back into the population.
        population.append(ga.mutate(ind1))
        population.append(ga.mutate(ind2))

      if population[0] == ga.OPTIMAL:
          break

    # Display the highest-ranked string after all generations have been iterated
    # over. This will be the closest string to the OPTIMAL string, meaning it
    # will have the smallest fitness value. Finally, exit the program.
    fittest_string = population[0]
    minimum_fitness = ga.fitness(population[0])

    for individual in population:
      ind_fitness = ga.fitness(individual)
      if ind_fitness <= minimum_fitness:
        fittest_string = individual
        minimum_fitness = ind_fitness

    print("Fittest String: %s" % fittest_string)
    with open("string-ga-{0}.txt".format(seed), "w") as f:
      f.write("Generations:{0}\n".format(total_gens))
      f.write("Fittest string: %s\n" % fittest_string)
