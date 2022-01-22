import random
from EvaluateIndividuals import evaluateIndividual


def findBestChrom(popularion):
    '''
    arg: population
    '''
    min_fitnes = inf
    best_chrom = 0
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
    
    popSz = len(population)
    index = random.randint(popSz,numInsert)
    population[index] = chrom
    return(population)
