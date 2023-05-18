
def get_pathlen(path,cityLocation):
    """
    Args:
        cityLocation - 2d positions of all avaliable cities
        Path - Path that you want to know the len of
    Returns:
        pathLen - len Of The Path
    """

    pathLen = 0

    for i in range(1:(len(path)-1)):
        indexFrom = path(i)
        indexTo = path(i+1)
        possFrom = cityLocation(indexFrom,:)
        possTo = cityLocation(indexTo,:)

        newLen = get_dist(possFrom,possTo)
        pathLen = pathLen + newLen


    possFrom = cityLocation(path(end),:)
    possTo = cityLocation(path(1),:)
    newLen = GetDist(possFrom,possTo)

    pathLen = pathLen + newLen
    return pathLen

