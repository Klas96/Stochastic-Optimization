import random

def GeneratePath(pheromoneLevel, visibility, alpha, beta):
    """
    Args:
        pheromoneLevel: Levels of pheromone at every path
        visibility: Visibility values
        alpha: Constant
        beta: Constant
    
    Returns:
        path: Generated path
    """

    indexForCitys = list(range(len(pheromoneLevel)))
    startingPoint = random.randint(0, len(pheromoneLevel) - 1)
    path = [startingPoint]

    for _ in range(len(pheromoneLevel) - 1):
        phermoneArray = pheromoneLevel[startingPoint].copy()
        phermoneArray[startingPoint] = None
        visibilityArray = visibility[startingPoint].copy()
        visibilityArray[startingPoint] = None

        nextCity = ChoosePath(phermoneArray, visibilityArray, alpha, beta)
        path.append(indexForCitys[nextCity])

        startingPoint = nextCity

    return path
