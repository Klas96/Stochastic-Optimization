from CrossPopulation import crossPopulation
from MutatePopulation import mutatePopulation
from InsertBestIndividual import insertChrom

def formNextGeneration(population):
    # Build Fittnnes Array


    #Cross Population
    population = crossPopulation(population)

    # Mutate Poulation
    population = mutatePopulation(population)

    # Find current best Chromsome
    
    # Insert best chromosome
    popularion = insertChrom(chrom, population)
    
    # Return Next Generation:
    return(population)
