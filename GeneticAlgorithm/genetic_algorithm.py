from .FormNextGen import formNextGeneration
from .EvaluateIndividuals import evaluateIndividual, fitnessFunction
from .InitializePopulation import initializePopulation
from .DecodeChromosone import decode_binary_chromosone


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
        population, best_chrom, max_fitnes = formNextGeneration(population)
        if verbose:
            print(f"Generation: {i} {max_fitnes=}")
    
    # Find Max in population
    maxFitValue = 0
    maxVariabels = []

    for chrom in population:
        fitValue = evaluateIndividual(chrom)
        if fitValue > maxFitValue:
            maxFitValue = fitValue
            maxVariabels = decode_binary_chromosone(chrom)
    
    finalAns = maxFitValue
    return finalAns, maxVariabels

def main():
    finalAns, variabel = GA(verbose = True)
    print(finalAns)
    print(variabel)

    print(f"{fitnessFunction(variabel)=}")

if __name__== "__main__":
    main()
