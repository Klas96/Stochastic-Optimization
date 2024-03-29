import random


def find_best_chrom(popularion, fittnes_fnc):
    '''
    arg: population
    ret: max_fitnes, best_chrom
    '''

    max_fitnes = -float('inf')
    best_chrom = popularion[0]

    for indi in popularion:
        fitness_value = indi.evaluate_individual(fittnes_fnc)
        if(fitness_value > max_fitnes):
            max_fitnes = fitness_value
            best_chrom = indi

    return(max_fitnes, best_chrom)



def insert_chromosone(chrom, population, num_insert = 1):
    '''
    Inserts chromsome at random index in population

    pre1: chromosome to be inserted
    pre2: population to insert chromsome into

    ret1: population with inserted chromsome
    '''
    
    population_size = population.shape[0]
    indexes = random.sample(range(population_size), num_insert)
    for idx in indexes:
        population[idx] = chrom
    
    return(population)
