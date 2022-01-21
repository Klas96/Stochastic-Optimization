from FormNextGen import formNextGeneration
from EvaluateIndividuals import evaluateIndividual
from InitializePopulation import initializePopulation
from DecodeChromosone import decodeBinaryChromosone

def GA(numGenerations = 250):
    # Init
    print("Running GA")
    print("Number of Generations: " + str(numGenerations))
    population = initializePopulation()

    # Evolve
    for i in range(numGenerations):
        print("Generation: " + str(i))
        population = formNextGeneration(population)
    
    # Return
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
    finalAns, variabel = GA()
    print(finalAns)
    print(variabel)

if __name__== "__main__":
    main()
