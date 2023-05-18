import random

def RunChoice(phermoneArray, visibilityArray, alpha, beta):
    """
    Args:
        phermoneArray: Pheromone levels
        visibilityArray: Visibility values
        alpha: Constant
        beta: Constant
    
    Returns:
        indexChosen: The chosen index
    """

    r = random.random()
    probLow = 0
    probHigh = 0
    indexChosen = 1

    # Calculate Normalizing Factor
    normalize = (phermoneArray ** alpha) * (visibilityArray ** beta)
    normalize = sum(normalize)

    # Loop through the allowed cities
    for i in range(1, len(phermoneArray)):
        probInter = (phermoneArray[i] ** alpha) * (visibilityArray[i] ** beta)
        probInter /= normalize

        probHigh = probLow + probInter
        if probLow <= r and r <= probHigh:
            indexChosen = i

        probLow = probHigh
    
    return indexChosen
