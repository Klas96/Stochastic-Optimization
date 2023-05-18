def UpdatePheromoneLevels(pheromoneLevel, deltaPheromoneLevel, rho):
    """
    Args:
        pheromoneLevel - levels of phermone at eveary path
        deltaPheromoneLevel -
        rho -
    Returns:
        pheromoneLevel: New and updated phermone levles
    """

    pheromoneLevel = pheromoneLevel*(1-rho) + deltaPheromoneLevel
    return(pheromoneLevel)