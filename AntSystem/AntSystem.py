import numpy as np
from . import GetNearestNeighbourPathlen

def main():
    AS()


def DeBug():
    # Parameters
    
    numberOfAnts = 50  # To do: Set to appropriate value.
    alpha = 1.0        # To do: Set to appropriate value.
    beta = 2.0         # To do: Set to appropriate value.
    rho = 0.7          # To do: set to appropriate value.

    node_positions = [(2,3), (1,3), (4,3)]
    number_of_nodes = len(node_positions)
    nearestNeighbourPathlen = GetNearestNeighbourPathlen(node_positions)
    tau0 = numberOfAnts/nearestNeighbourPathlen
    pheromoneLevel = InitializePheromoneLevels(number_of_nodes, tau0)
    visibility = get_visibility(node_positions)

    path = GeneratePath(pheromoneLevel, visibility, alpha, beta)
    GetPathlen(path,cityLocation)
    GetPathlen(randperm(50),cityLocation)
    GetPathlen(randperm(50),cityLocation)
    GetPathlen(randperm(50),cityLocation)

class AS():
    """
    Optimization Algorithm for solving the traveling sales man problem.
    """
    def __init__():
        pass


    # Ant system (AS) for Traveling Sales Man Problem (TSP)

    # Data
    
    #addpath('/TSPgraphics')
    cityLocation = LoadCityLocations()
    numberOfCities = len(cityLocation)

    # Parameters
    
    numberOfAnts = 50  # To do: Set to appropriate value.
    alpha = 1.0        # To do: Set to appropriate value.
    beta = 2.0         # To do: Set to appropriate value.
    rho = 0.7          # To do: set to appropriate value.

    # To do: Write the GetNearestNeighbourPathlen function
    nearestNeighbourPathlen = GetNearestNeighbourPathlen(cityLocation)
    tau0 = numberOfAnts/nearestNeighbourPathlen

    targetPathlen = 123.0
    targetPathlen = 124.0
    targetPathlen = 125.0
    targetPathlen = 125.5
    
    # Initialization

    range = [0 20 0 20]
    #tspFigure = InitializeTspPlot(cityLocation, range)
    #connection = InitializeConnections(cityLocation)

    #pheromoneLevel = InitializePheromoneLevels(numberOfCities, tau0)
    #visibility = GetVisibility(cityLocation)

    
    # Main loop
    
    minimumPathlen = float('infinity')

    iIteration = 0

    while (minimumPathlen > targetPathlen):
        iIteration = iIteration + 1

        # Generate paths:

        pathCollection = []
        pathlenCollection = []
        for k in range(1,numberOfAnts):
            path = GeneratePath(pheromoneLevel, visibility, alpha, beta)
            pathlen = get_path_len(path,cityLocation)
            if (pathlen < minimumPathlen):
                minimumPathlen = pathlen
                minimum = path
                print(f"Iteration {iIteration}, ant {k}: path len = {minimumPathlen}")
                PlotPath(connection,cityLocation,path)
            pathCollection =[pathCollection.append(path)

    pathlenCollection = pathlenCollection.append(pathlen)

     # Update pheromone levels

    deltaPheromoneLevel = ComputeDeltaPheromoneLevels(pathCollection,pathlenCollection)
    pheromoneLevel = UpdatePheromoneLevels(pheromoneLevel,deltaPheromoneLevel,rho)
    
    PlotPath(connection,cityLocation,minimum)
    title(['Traversions: ' num2str(iIteration) ' len: ' num2str(minimumPathlen)])


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


#Pre:
  #pathCollection: A collection of all paths
  #pathlenCollection: A colection of all path lens
#Ret
  #Matrix ofpathCollection the Phermone Updat levels decide py the path
def ComputeDeltaPheromoneLevels(pathCollection,pathlenCollection):
    """
    Args:

    Returns:

    """
    deltaPheromoneLevel = zeros(len(pathCollection(1,:)),len(pathCollection(1,:)))

    for iPath in range(1,len(pathCollection(:,1))):
        update = 1/pathlenCollection(iPath)
        for iCity = 1:(len(pathCollection(1,:))-1):

            fromCity = pathCollection(iPath,iCity)
            toCity = pathCollection(iPath,iCity+1)

        deltaPheromoneLevel(fromCity,toCity) = deltaPheromoneLevel(fromCity,toCity) + update
        #deltaPheromoneLevel(toCity,fromCity) = deltaPheromoneLevel(toCity,fromCity) + update
    
    return(deltaPheromoneLevel)



def GeneratePath(pheromoneLevel, visibility, alpha, beta):
    """
    Args:
        pheromoneLevel -levels of phermone at eveary path
        visibility
        alpha: Const
        beta: Const
        tabuList - List of allready vivited Nodes
    
    Returns:
        path: Path generated
    """

    indexForCitys = range(1,len(pheromoneLevel))
    #tabuList = true(1,len(pheromoneLevel(:,1)))
    #cityIndexList = 1:len(pheromoneLevel(:,1))
    startingPoint = randi(len(pheromoneLevel(1,:)))
    path = [startingPoint]

    for i in range(1,(len(pheromoneLevel(1,:))-1)):

        # tabuList(startingPoint) = false
        # Take This one
        phermoneArray = pheromoneLevel(startingPoint,:)
        phermoneArray(startingPoint) = []
        visibilityArray = visibility(startingPoint,:)
        visibilityArray(startingPoint) = []
        # Remove
        pheromoneLevel(startingPoint,:) = []
        pheromoneLevel(:,startingPoint) = []
        visibility(startingPoint,:) = []
        visibility(:,startingPoint) = []
        indexForCitys(startingPoint) = []
        nextCity = ChoosePath(phermoneArray, visibilityArray, alpha, beta)

        path = [path indexForCitys(nextCity)]
        startingPoint = nextCity

    return(path)


def  ChoosePath(phermoneArray, visibilityArray, alpha, beta, tabuList):
    '''
    Args:
        startingPoint
        #pheromoneLevel: levels of phermone at eveary path
        #visibility
        #alpha: Const
        #beta: Const
        #tabuList: Boulean list. Faslse - visited
    Returns:
        #nextVeretex: Next Veretex chosen
        #TestStaus: OK
        #Dependencies: RunChoise
    '''

    nextVeretex = RunChoise(phermoneArray,visibilityArray,alpha, beta)
    return(nextVeretex)


def  RunChoise(phermoneArray,visibilityArray,alpha, beta)
    """
        Args:
        startingPoint
        tabuFreePhermone: Phermone Levels where the tabu poistions have been removed
        tabuFreeVisibility: visibility where the tabu poistions have been removed
        alpha: Const
        beta: Const
        Ret:
        indexChosen: The index chosen
        TestStaus: OK
        Dependencies: None
    """

    r = rand
    probLow = 0
    probHigh = 0
    indexChosen = 1

    # Making Normalizing Factor
    normlize = phermoneArray**alpha
    normlize = sum(normlize*visibilityArray**beta)

    # Loop Through the allowed cities
    for i in range(1:len(phermoneArray)):
        probInter = phermoneArray(i)**alpha
        probInter = probInter*visibilityArray(i)**beta
        probInter = probInter/normlize

        probHigh = probLow + probInter
        if probLow <= r and r <= probHigh:
            indexChosen = i
        
        probLow = probHigh
    return(indexChosen)




def get_visibility(cityLocation)
    """
    Args:
        cityLocation - 2d positions of all avaliable cities
    Returns:
        nearNeigPathLen - len Of The Nearest Naigbhor Path
    """

    numberOfCities = len(cityLocation(:,1))
    visib = zeros(numberOfCities,numberOfCities)

    neaNerglen = 0
    neaNergIndex = 0

    for i in range(1,len(cityLocation(:,1))):
        for j in range(1,len(cityLocation)):
        if(i != j)
            neaNerglen = GetDist(cityLocation(i,:), cityLocation(j,:))
            visib(i,j) = 1/neaNerglen

    return visib


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



def get_nearest_neighbour(cityPos, cityLocations):
    """
    Args:
        2d pos cityPos, array of 2d pos cityLocations
    
    Returns:
        index of nearest path, lenNearest path
    """
    indexNearest = 0

    distMin = inf
    for i in range(1,len(cityLocations)):
        dist = GetDist(cityPos, cityLocations(i))
        if(dist < distMin):
            distMin = dist
        indexNearest = i

    neaNergIndex = indexNearest
    neaNerglen = distMin
    return(neaNerglen, neaNergIndex)



def get_dist(pos1,pos2):
    """
    Args:
        2d pos cityPos, array of 2d pos cityLocations
        pos1,pos2: 2d positions
    
    Returns:
        distance Between positions
    """
    
    # X Pos
    xDiff = pos1(1) - pos2(1)
    
    # Y Pos
    yDiff = pos1(2) - pos2(2)

    dist = sqrt(xDiff**2 + yDiff**2)
    
    return(dist)