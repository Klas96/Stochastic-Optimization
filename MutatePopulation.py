import random


#Pre:population
#Ret:mutated population
def mutatePopulation(population):
    for i in range(len(population)):
        chrom = population[i]
        chromMut = mutateChromosone(chrom)
        population[i] = chromMut
    return(population)


#Pre: chrom, a crhomosone, pMut a Mutate probability
#Ret: chroMut Mutated chromosone
def mutateChromosone(chrom):
    pMut = 0.05
    chromMut = chrom
    for i in range(chrom.size):
        if(random.uniform(0, 1) < pMut):
            chromMut[i] = abs(chrom[i]-1)
    return(chromMut)
