from .CrossPopulation import crossPopulation
from .MutatePopulation import mutatePopulation
from .InsertBestIndividual import insert_chromosone, find_best_chrom

def form_next_generation(population, verbose = False):
    '''
    pre: population
    return: population, best_chrom, min_fitness
    '''
    # Build Fittnnes Array

    # Find current best Chromsome
    max_fitness, best_chrom = find_best_chrom(population)

    #Cross Population
    population = crossPopulation(population)

    # Mutate Poulation
    population = mutatePopulation(population)

    # Insert best chromosome
    population = insert_chromosone(best_chrom, population)
    
    # Return Next Generation:
    return(population, best_chrom, max_fitness)
