def InitializePheromoneLevels(numberOfCities, tau0):
    '''
    Args:
        numberOfCities:
        tau0: Starting phermone

    Returns:
        pheromoneLevel: Matrix of Paths With starting Phermone.
        TestStaus: None
        Dependencies: None
    '''

    pheromoneLevel(1:numberOfCities,1:numberOfCities) = tau0
    return(pheromoneLevel)
