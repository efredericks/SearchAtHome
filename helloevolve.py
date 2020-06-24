"""
helloevolve.py implements a genetic algorithm that starts with a base
population of randomly generated strings, iterates over a certain number of
generations while implementing 'natural selection', and prints out the most fit
string.

The parameters of the simulation can be changed by modifying one of the many
global variables. To change the "most fit" string, modify OPTIMAL. POP_SIZE
controls the size of each generation, and GENERATIONS is the amount of 
generations that the simulation will loop through before returning the fittest
string.

This program subject to the terms of the BSD license listed below.

---

Copyright (c) 2011 Colin Drake

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import random

class StringGA(object):
    def __init__(self, pop_size, generations, optimal, seed):
      random.seed(seed)

      #OPTIMAL     = "Hello, World"
      self.OPTIMAL     = optimal
      self.DNA_SIZE    = len(self.OPTIMAL)
      self.POP_SIZE    = pop_size
      self.GENERATIONS = generations

      self.population  = [] 

    #
    # Helper functions
    # These are used as support, but aren't direct GA-specific functions.
    #
    def weighted_choice(self, items):
      """
      Chooses a random element from items, where items is a list of tuples in
      the form (item, weight). weight determines the probability of choosing its
      respective item. Note: this function is borrowed from ActiveState Recipes.
      """
      weight_total = sum((item[1] for item in items))
      n = random.uniform(0, weight_total)
      for item, weight in items:
        if n < weight:
          return item
        n = n - weight
      return item

    def random_char(self):
      """
      Return a random character between ASCII 32 and 126 (i.e. spaces, symbols,
      letters, and digits). All characters returned will be nicely printable.
      """
      return chr(int(random.randrange(32, 126, 1)))

    def random_population(self):
      """
      Return a list of POP_SIZE individuals, each randomly generated via iterating
      DNA_SIZE times to generate a string of random characters with random_char().
      """
      pop = []
      for i in range(self.POP_SIZE):
        dna = ""
        for c in range(self.DNA_SIZE):
          dna += self.random_char()
        pop.append(dna)
      return pop

    #
    # GA functions
    # These make up the bulk of the actual GA algorithm.
    #

    def fitness(self, dna):
      """
      For each gene in the DNA, this function calculates the difference between
      it and the character in the same position in the OPTIMAL string. These values
      are summed and then returned.
      """
      fitness = 0
      for c in range(self.DNA_SIZE):
        fitness += abs(ord(dna[c]) - ord(self.OPTIMAL[c]))
      return fitness

    def mutate(self, dna):
      """
      For each gene in the DNA, there is a 1/mutation_chance chance that it will be
      switched out with a random character. This ensures diversity in the
      population, and ensures that is difficult to get stuck in local minima.
      """
      dna_out = ""
      mutation_chance = 100
      for c in range(self.DNA_SIZE):
        if int(random.random()*mutation_chance) == 1:
          dna_out += self.random_char()
        else:
          dna_out += dna[c]
      return dna_out
    
    def crossover(self, dna1, dna2):
      """
      Slices both dna1 and dna2 into two parts at a random index within their
      length and merges them. Both keep their initial sublist up to the crossover
      index, but their ends are swapped.
      """
      pos = int(random.random()*self.DNA_SIZE)
      return (dna1[:pos]+dna2[pos:], dna2[:pos]+dna1[pos:])

    #
    # Main driver
    # Generate a population and simulate GENERATIONS generations.
    #
    def main(self):

      # Generate initial population. This will create a list of POP_SIZE strings,
      # each initialized to a sequence of random characters.
      population = self.random_population()
    
      # Simulate all of the generations.
      done = False
      winner = ""
      for generation in range(self.GENERATIONS):
        print("Generation %s... Random sample: '%s'" % (generation, population[0]))
        weighted_population = []

        # Add individuals and their respective fitness levels to the weighted
        # population list. This will be used to pull out individuals via certain
        # probabilities during the selection phase. Then, reset the population list
        # so we can repopulate it after selection.
        for individual in population:
          fitness_val = self.fitness(individual)

          # Generate the (individual,fitness) pair, taking in account whether or
          # not we will accidently divide by zero.
          if fitness_val == 0:
            pair = (individual, 1.0)
          else:
            pair = (individual, 1.0/fitness_val)

          weighted_population.append(pair)

          if (individual == self.OPTIMAL):
              winner = individual
              done = True

        if done:
            print("Found the answer early at Generation {0}! [{1}]".format(generation,winner))
            break

        population = []

        # Select two random individuals, based on their fitness probabilites, cross
        # their genes over at a random point, mutate them, and add them back to the
        # population for the next iteration.
        for _ in range(int(self.POP_SIZE/2)):
          # Selection
          ind1 = self.weighted_choice(weighted_population)
          ind2 = self.weighted_choice(weighted_population)

          # Crossover
          ind1, ind2 = self.crossover(ind1, ind2)

          # Mutate and add back into the population.
          population.append(self.mutate(ind1))
          population.append(self.mutate(ind2))

        if population[0] == self.OPTIMAL:
            break

      # Display the highest-ranked string after all generations have been iterated
      # over. This will be the closest string to the OPTIMAL string, meaning it
      # will have the smallest fitness value. Finally, exit the program.
      fittest_string = population[0]
      minimum_fitness = self.fitness(population[0])

      for individual in population:
        ind_fitness = self.fitness(individual)
        if ind_fitness <= minimum_fitness:
          fittest_string = individual
          minimum_fitness = ind_fitness

      print("Fittest String: %s" % fittest_string)
