import random

def GetDist(pos1, pos2):
    """
    Distance betwen pos1 and pos2
    """

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
        neaNerglen, neaNergIndex = get_nearest_neighbour(cityPos, cityLocation)
        lenNearestTot += neaNerglen

    # Connect
    dist = GetDist(cityPos, firstCityPos)
    lenNearestTot += dist

    nearNeigPathLen = lenNearestTot
    return nearNeigPathLen


def get_nearest_neighbour(cityPos, cityLocations):
    """
    Args:
        2d pos cityPos, array of 2d pos cityLocations
    
    Returns:
        index of nearest path, lenNearest path
    """
    indexNearest = 0

    distMin = float('inf')
    for i in range(1,len(cityLocations)):
        dist = GetDist(cityPos, cityLocations(i))
        if(dist < distMin):
            distMin = dist
        indexNearest = i

    neaNergIndex = indexNearest
    neaNerglen = distMin

    return(neaNerglen, neaNergIndex)