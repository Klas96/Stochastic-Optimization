from .cross_population import cross_population
from .mutate_population import mutate_population
from .insert_best_individual import insert_chromosone, find_best_chrom
from .evaluate_individuals import function_to_mimimixe

def form_next_generation(population, verbose = False, target_function = function_to_mimimixe):
    '''
    pre: population
    return: population, best_chrom, min_fitness
    '''
    # Build Fittnnes Array

    # Find current best Chromsome
    max_fitness, best_chrom = find_best_chrom(population, target_function = target_function)

    #Cross Population
    population = cross_population(population, target_function = target_function)

    # Mutate Poulation
    population = mutate_population(population)

    # Insert best chromosome
    population = insert_chromosone(best_chrom, population)
    
    # Return Next Generation:
    return(population, best_chrom, max_fitness)
