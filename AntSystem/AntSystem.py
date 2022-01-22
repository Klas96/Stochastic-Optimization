def main():
    AS()


def DeBug():
    # Parameters
    
    numberOfAnts = 50  # To do: Set to appropriate value.
    alpha = 1.0        # To do: Set to appropriate value.
    beta = 2.0         # To do: Set to appropriate value.
    rho = 0.7          # To do: set to appropriate value.

    addpath('/TSPgraphics')

    cityLocation = LoadCityLocations()
    numberOfCities = len(cityLocation)
    nearestNeighbourPathlen = GetNearestNeighbourPathlen(cityLocation)
    tau0 = numberOfAnts/nearestNeighbourPathlen
    pheromoneLevel = InitializePheromoneLevels(numberOfCities, tau0)
    visibility = GetVisibility(cityLocation)

    path = GeneratePath(pheromoneLevel, visibility, alpha, beta)
    GetPathlen(path,cityLocation)
    GetPathlen(randperm(50),cityLocation)
    GetPathlen(randperm(50),cityLocation)
    GetPathlen(randperm(50),cityLocation)

def AS():
    
    # Ant system (AS) for TSP.

    # Data
    
    addpath('/TSPgraphics')
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
    tspFigure = InitializeTspPlot(cityLocation, range)
    connection = InitializeConnections(cityLocation)

    pheromoneLevel = InitializePheromoneLevels(numberOfCities, tau0)
    visibility = GetVisibility(cityLocation)

    
    # Main loop
    
    minimumPathlen = float('infinity')

    iIteration = 0

    while (minimumPathlen > targetPathlen)
     iIteration = iIteration + 1

     # Generate paths:

     pathCollection = []
     pathlenCollection = []
     for k = 1:numberOfAnts
      path = GeneratePath(pheromoneLevel, visibility, alpha, beta)
      pathlen = GetPathlen(path,cityLocation)
      if (pathlen < minimumPathlen)
        minimumPathlen = pathlen
        minimum = path
        disp(sprintf('Iteration #d, ant #d: path len = #.5f',iIteration,k,minimumPathlen))
        PlotPath(connection,cityLocation,path)
      end
      pathCollection = [pathCollection path]

      pathlenCollection = [pathlenCollection pathlen]
     end

     # Update pheromone levels

     deltaPheromoneLevel = ComputeDeltaPheromoneLevels(pathCollection,pathlenCollection)
     pheromoneLevel = UpdatePheromoneLevels(pheromoneLevel,deltaPheromoneLevel,rho)

    end
    
    PlotPath(connection,cityLocation,minimum)
    title(['Traversions: ' num2str(iIteration) ' len: ' num2str(minimumPathlen)])
end


def UpdatePheromoneLevels(pheromoneLevel, deltaPheromoneLevel, rho):
    '''
    Pre:
    pheromoneLevel: levels of phermone at eveary path
    deltaPheromoneLevel:
    rho:
    Ret:
    pheromoneLevel: New and updated phermone levles
    TestStaus: None
    Dependencies:
    '''

    pheromoneLevel = pheromoneLevel*(1-rho) + deltaPheromoneLevel
    return(pheromoneLevel)


#Pre:
  #pathCollection: A collection of all paths
  #pathlenCollection: A colection of all path lens
#Ret
  #Matrix ofpathCollection the Phermone Updat levels decide py the path
def ComputeDeltaPheromoneLevels(pathCollection,pathlenCollection):

    deltaPheromoneLevel = zeros(len(pathCollection(1,:)),len(pathCollection(1,:)))

    for iPath in  range(1:len(pathCollection(:,1))):
        update = 1/pathlenCollection(iPath)
        for iCity = 1:(len(pathCollection(1,:))-1)

        fromCity = pathCollection(iPath,iCity)
        toCity = pathCollection(iPath,iCity+1)

        deltaPheromoneLevel(fromCity,toCity) = deltaPheromoneLevel(fromCity,toCity) + update
        #deltaPheromoneLevel(toCity,fromCity) = deltaPheromoneLevel(toCity,fromCity) + update
    
    return(deltaPheromoneLevel)



def  = GeneratePath(pheromoneLevel, visibility, alpha, beta)
    '''
    Pre:
    pheromoneLevel: levels of phermone at eveary path
    visibility
    alpha: Const
    beta: Const
    tabuList: List of allready vivited Nodes
    Ret:
    path: Path generated
    TestStaus: OK
    Dependencies: ChoosePath
    Problem Kommer gå från sig själv till sig själv hela tiden??
    '''

    indexForCitys = 1:len(pheromoneLevel)
    #tabuList = true(1,len(pheromoneLevel(:,1)))
    #cityIndexList = 1:len(pheromoneLevel(:,1))
    startingPoint = randi(len(pheromoneLevel(1,:)))
    path = [startingPoint]

    for i = 1:(len(pheromoneLevel(1,:))-1)

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


def  ChoosePath(phermoneArray, visibilityArray, alpha, beta,tabuList)
    '''
    #Pre:
    #startingPoint
    #pheromoneLevel: levels of phermone at eveary path
    #visibility
    #alpha: Const
    #beta: Const
    #tabuList: Boulean list. Faslse - visited
    #Ret:
    #nextVeretex: Next Veretex chosen
    #TestStaus: OK
    #Dependencies: RunChoise
    '''

    nextVeretex = RunChoise(phermoneArray,visibilityArray,alpha, beta)
    return(nextVeretex)


def  RunChoise(phermoneArray,visibilityArray,alpha, beta)
    '''
        Pre:
        startingPoint
        tabuFreePhermone: Phermone Levels where the tabu poistions have been removed
        tabuFreeVisibility: visibility where the tabu poistions have been removed
        alpha: Const
        beta: Const
        Ret:
        indexChosen: The index chosen
        TestStaus: OK
        Dependencies: None
    '''

    r = rand
    probLow = 0
    probHigh = 0
    indexChosen = 1

    #Making Normalizing Factor
    normlize = phermoneArray**alpha
    normlize = sum(normlize*visibilityArray**beta)

    # Loop Through the allowed cities
    for i = 1:len(phermoneArray)
        probInter = phermoneArray(i)**alpha
        probInter = probInter*visibilityArray(i)**beta
        probInter = probInter/normlize

        probHigh = probLow + probInter
        if probLow <= r and r <= probHigh
        indexChosen = i
        end
        probLow = probHigh
    return(indexChosen)



def pheromoneLevel = InitializePheromoneLevels(numberOfCities, tau0)
    '''
    Pre:
    numberOfCities:
    tau0: Starting phermone
    Ret:
    pheromoneLevel: Matrix of Paths With starting Phermone.
    TestStaus: None
    Dependencies: None
    '''

    pheromoneLevel(1:numberOfCities,1:numberOfCities) = tau0
    return(pheromoneLevel)

def  = GetVisibility(cityLocation)
    '''
    Pre:
    cityLocation: 2d positions of all avaliable cities
    Ret:
    #nearNeigPathLen: len Of The Nearest Naigbhor Path
    TestStaus: None
    Dependencies: GetDist
    '''

    numberOfCities = len(cityLocation(:,1))
    visib = zeros(numberOfCities,numberOfCities)

    neaNerglen = 0
    neaNergIndex = 0

    for i = 1:len(cityLocation(:,1))
        for j = 1:len(cityLocation)
        if(i ~= j)
            neaNerglen = GetDist(cityLocation(i,:), cityLocation(j,:))
            visib(i,j) = 1/neaNerglen

    return(visib)


def  = GetPathlen(path,cityLocation)
    '''
    Pre:
    cityLocation: 2d positions of all avaliable cities
    Path: Path that you want to know the len of
    Ret:
    pathLen: len Of The Path
    TestStaus: None
    Dependencies: GetDist
    '''

    pathLen = 0

    for i = 1:(len(path)-1)
        indexFrom = path(i)
        indexTo = path(i+1)
        possFrom = cityLocation(indexFrom,:)
        possTo = cityLocation(indexTo,:)

        newLen = GetDist(possFrom,possTo)
        pathLen = pathLen + newLen


    possFrom = cityLocation(path(end),:)
    possTo = cityLocation(path(1),:)
    newLen = GetDist(possFrom,possTo)

    pathLen = pathLen + newLen
    return(pathLen)



def  GetNearestNeighbourPathlen(cityLocation)
    '''
    Pre:
    cityLocation: 2d positions of all avaliable cities
    ret
    nearNeigPathLen: len Of The Nearest Naigbhor Path
    TestStaus: None
    Dependencies: GetNearestNeighbour
    '''
    nearNeigPathLen = 0
    lenNearestTot = 0
    neaNergIndex = randi(len(cityLocation(:,1)))
    firstCityPos = cityLocation(neaNergIndex,:)
    for cityIndex = 1:(len(cityLocation(:,1))-1)
        cityPos = cityLocation(neaNergIndex,:)
        cityLocation(neaNergIndex,:) = []
        [neaNerglen neaNergIndex] = GetNearestNeighbour(cityPos, cityLocation)
        lenNearestTot = lenNearestTot + neaNerglen

    # Conect
    dist = GetDist(cityPos, firstCityPos)
    lenNearestTot = lenNearestTot + neaNerglen

    nearNeigPathLen = lenNearestTot
    return(nearNeigPathLen)



def GetNearestNeighbour(cityPos, cityLocations)
    '''
    Pre 2d pos cityPos, array of 2d pos cityLocations
    ret index of nearest path, lenNearest path
    TestStaus: None
    Dependencies: GetDist
    '''
    indexNearest = 0

    distMin = inf
    for i = 1:(len(cityLocations(:,1)))
        dist = GetDist(cityPos, cityLocations(i,:))
        if(dist < distMin)
        distMin = dist
        indexNearest = i

    neaNergIndex = indexNearest
    neaNerglen = distMin
    return(neaNerglen, neaNergIndex)



def dist = GetDist(pos1,pos2)
    '''
    Pre 2d pos cityPos, array of 2d pos cityLocations
    pos1,pos2: 2d positions
    ret distance Between positions
    TestStaus: None
    Dependencies: None
    '''
    
    # X Pos
    xDiff = pos1(1) - pos2(1)
    
    # Y Pos
    yDiff = pos1(2) - pos2(2)

    dist = sqrt(xDiff**2 + yDiff**2)
    
    return(dist)