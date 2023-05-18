def  get_nearest_neighbour_pathlen(cityLocation):
    """
    Args:
        cityLocation: 2d positions of all avaliable cities
    
    Returns:
        nearNeigPathLen: len Of The Nearest Naigbhor Path
    
    """
    nearNeigPathLen = 0
    lenNearestTot = 0
    neaNergIndex = randi(len(cityLocation(:,1)))
    firstCityPos = cityLocation(neaNergIndex,:)
    for cityIndex in range(1,(len(cityLocation(:,1))-1))
        cityPos = cityLocation(neaNergIndex,:)
        cityLocation(neaNergIndex,:) = []
        neaNerglen, neaNergIndex = GetNearestNeighbour(cityPos, cityLocation)
        lenNearestTot = lenNearestTot + neaNerglen

    # Conect
    dist = GetDist(cityPos, firstCityPos)
    lenNearestTot = lenNearestTot + neaNerglen

    nearNeigPathLen = lenNearestTot
    return(nearNeigPathLen)