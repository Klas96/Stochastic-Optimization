import numpy as np

def get_visibility(cityLocation):
    """
    Args:
        cityLocation: 2D positions of all available cities
    
    Returns:
        visib: Matrix representing the visibility between cities
    """
    numberOfCities = len(cityLocation)
    visib = np.zeros((numberOfCities, numberOfCities))

    for i in range(len(cityLocation)):
        for j in range(len(cityLocation)):
            if i != j:
                neaNerglen = GetDist(cityLocation[i], cityLocation[j])
                visib[i, j] = 1 / neaNerglen

    return visib
