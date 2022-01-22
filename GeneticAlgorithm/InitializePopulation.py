import numpy as np

#Pre: Number of Individuals In Populations
#Ret: Population, List of populationSize number of numpy arrays§
def initializePopulation(popSz = 100, number_of_variabels = 3):
    print("Creating popoplation with size " + str(popSz))
    population = []
    #create popoplation
    for i in range(popSz):
        #create Init Individual
        individual = createBinaryChromosome(number_of_variabels)
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
