import random
from individual import Individual

def mutate_population(population):
    '''
    Pre:population
    Ret:mutated population
    '''
    
    for i in range(len(population)):
        chrom = population[i]
        chromMut = mutate_chromosone(chrom)
        population[i] = chromMut
    return(population)


def mutate_chromosone(chrom, pMut = 0.05):
    '''
    Pre: chrom, a crhomosone, pMut a Mutate probability
    Ret: chroMut Mutated chromosone
    '''

    chromMut = chrom
    for i in range(chrom.size):
        if(random.uniform(0, 1) < pMut):
            chromMut[i] = abs(chrom[i]-1)
    return(chromMut)
