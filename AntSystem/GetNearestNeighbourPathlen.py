import random

def get_nearest_neighbour_pathlen(cityLocation):
    """
    Args:
        cityLocation: 2D positions of all available cities
    
    Returns:
        nearNeigPathLen: Length of the Nearest Neighbor Path
    """
    nearNeigPathLen = 0
    lenNearestTot = 0
    neaNergIndex = random.randint(0, len(cityLocation)-1)
    firstCityPos = cityLocation[neaNergIndex]

    for cityIndex in range(1, len(cityLocation)):
        cityPos = cityLocation[neaNergIndex]
        del cityLocation[neaNergIndex]
        neaNerglen, neaNergIndex = GetNearestNeighbour(cityPos, cityLocation)
        lenNearestTot += neaNerglen

    # Connect
    dist = GetDist(cityPos, firstCityPos)
    lenNearestTot += dist

    nearNeigPathLen = lenNearestTot
    return nearNeigPathLen
