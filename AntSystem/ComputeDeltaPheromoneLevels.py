import numpy as np

def ComputeDeltaPheromoneLevels(pathCollection, pathlenCollection):
    """
    Args:
        pathCollection: A collection of all paths
        pathlenCollection: A collection of all path lengths
    
    Returns:
        deltaPheromoneLevel: Matrix of pathCollection representing the pheromone update levels
    """
    deltaPheromoneLevel = np.zeros((len(pathCollection[0]), len(pathCollection[0])))

    for iPath in range(len(pathCollection)):
        update = 1 / pathlenCollection[iPath]
        for iCity in range(len(pathCollection[0]) - 1):

            fromCity = pathCollection[iPath][iCity]
            toCity = pathCollection[iPath][iCity + 1]

            deltaPheromoneLevel[fromCity, toCity] += update
            #deltaPheromoneLevel[toCity, fromCity] += update

    return deltaPheromoneLevel

