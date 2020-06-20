import random
def insertChrom(chrom,population):
    numInsert = 1
    popSz = len(population)
    index = random.randint(popSz,numInsert)
    population[index] = chrom
    return(population)
