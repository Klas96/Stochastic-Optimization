from .FormNextGen import formNextGeneration
from .EvaluateIndividuals import evaluateIndividual, fitnessFunction
from .InitializePopulation import initializePopulation
from .DecodeChromosone import decodeBinaryChromosone


def GA(numGenerations = 250, verbose = False):
    '''
    arg numGenerations = 250
    verbose = False

    finding 
    '''
    if verbose:
        print("Running GA")
        print("Number of Generations: " + str(numGenerations))
    
    population = initializePopulation()
    
    # Evolve
    for i in range(numGenerations):
        if verbose:
            print("Generation: " + str(i))
        population, best_chrom, min_fitnes = formNextGeneration(population)
    
    # Find Max in population
    maxFitValue = 0
    maxVariabels = []

    for chrom in population:
        fitValue = evaluateIndividual(chrom)
        if fitValue > maxFitValue:
            maxFitValue = fitValue
            maxVariabels = decodeBinaryChromosone(chrom)
    
    finalAns = maxFitValue
    return finalAns, maxVariabels

def main():
    finalAns, variabel = GA(verbose = True)
    print(finalAns)
    print(variabel)

    print(f"{fitnessFunction(variabel)=}")

if __name__== "__main__":
    main()
