import numpy as np

def initialize_population(population_size = 100, number_of_variabels = 3):
    '''
    Pre: Number of Individuals In Populations
    Ret: Population, List of populationSize number of numpy arrays§
    '''
    variabel_length = 25
    population = np.random.randint(0,2,(population_size,number_of_variabels*variabel_length))
    return(population)


def initializePopulationList(population_size = 100, number_of_variabels = 3):
    '''
    Pre: Number of Individuals In Populations
    Ret: Population, List of populationSize number of numpy arrays

    The Good thing with this is that it can hold chromosomes with diffrent lengths
    '''

    print("Creating popoplation with size " + str(population_size))
    #population = np.array()
    population = []
    #create popoplation
    for i in range(population_size):
        #create Init Individual
        individual = createBinaryChromosome(number_of_variabels)
        #append Individual
        population.append(individual)
        #hstack
        #population = np.concatenate((population, individual))

    #population = np.array(population)
    variabel_length = 25
    population = np.random.randint(0,2,(population_size,number_of_variabels*variabel_length))
    return(population)


def createBinaryChromosome(numberOfVariabels = 1, variabel_length = 25):
    
    chromLen = variabel_length*numberOfVariabels
    chrom = np.random.randint(2,size=chromLen)

    return(chrom)



def createRealNumberChromosone(numberOfVariabels = 1, range = [0,1]):
    pass
