import numpy as np

def InitializePheromoneLevels(numberOfCities, tau0):
    '''
    Args:
        numberOfCities: Number of cities in the problem
        tau0: Starting pheromone level

    Returns:
        pheromoneLevel: Matrix of paths with starting pheromone levels
    '''

    pheromoneLevel = np.full((numberOfCities, numberOfCities), tau0)
    return pheromoneLevel

