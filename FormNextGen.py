from CrossPopulation import crossPopulation
from MutatePopulation import mutatePopulation

def formNextGeneration(population):
    #Build Fittnnes Array

    #Cross Population
    population = crossPopulation(population)
    #Mutate Poulation
    population = mutatePopulation(population)
    #Insert Best Individual
    
    #Return Next Generation:

    return(population)
