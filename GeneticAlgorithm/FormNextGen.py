from .CrossPopulation import crossPopulation
from .MutatePopulation import mutatePopulation
from .InsertBestIndividual import insertChrom, find_best_chrom

def formNextGeneration(population, verbose = False):
    # Build Fittnnes Array


    #Cross Population
    population = crossPopulation(population)

    # Mutate Poulation
    population = mutatePopulation(population)

    # Find current best Chromsome
    min_fitness, best_chrom = find_best_chrom(population)

    if(verbose):
        print(f"{min_fitness=}")

    # Insert best chromosome
    population = insertChrom(best_chrom, population)
    
    # Return Next Generation:
    return(population, best_chrom, min_fitness)
