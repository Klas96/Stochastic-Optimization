import random

from .EvaluateIndividuals import evaluateIndividual


def find_best_chrom(popularion):
    '''
    arg: population
    '''
    min_fitnes = float('inf')
    best_chrom = popularion[0]
    for chrom in popularion:
        fitness_value = evaluateIndividual(chrom)
        if(fitness_value < min_fitnes):
            min_fitnes = fitness_value

    return(min_fitnes, best_chrom)



def insertChrom(chrom, population, num_insert = 1):
    '''
    Inserts chromsome at random index in population

    pre1: chromosome to be inserted
    pre2: population to insert chromsome into

    ret1: population with inserted chromsome
    '''
    
    population_size = len(population)
    indexes = random.sample(range(population_size), num_insert)
    for idx in indexes:
        population[idx] = chrom
    
    return(population)
