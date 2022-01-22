import numpy as np

#Pre: Number of Individuals In Populations
#Ret: Population, List of populationSize number of numpy arrays§
def initializePopulation(popSz = 100):
    print("Creating popoplation with sieze " + str(popSz))
    population = []
    numberOfVariabels = 3
    #create popoplation
    for i in range(popSz):
        #create Init Individual
        individual = createBinaryChromosome(numberOfVariabels)
        #append Individual
        population.append(individual)
    return(population)


def createBinaryChromosome(numberOfVariabels = 1):
    variabelLength = 25
    chromLen = 25*numberOfVariabels
    chrom = np.random.randint(2,size=chromLen)
    return(chrom)

def createRealNumberChromosone(numberOfVariabels = 1, range = [0,1]):
    pass
