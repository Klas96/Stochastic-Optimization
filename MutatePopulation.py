import random

def mutatePopulation(population):
    '''
    Pre:population
    Ret:mutated population
    '''
    for i in range(len(population)):
        chrom = population[i]
        chromMut = mutateChromosone(chrom)
        population[i] = chromMut
    return(population)


def mutateChromosone(chrom):
    '''
    Pre: chrom, a crhomosone, pMut a Mutate probability
    Ret: chroMut Mutated chromosone
    '''
    pMut = 0.05
    chromMut = chrom
    for i in range(chrom.size):
        if(random.uniform(0, 1) < pMut):
            chromMut[i] = abs(chrom[i]-1)
    return(chromMut)
