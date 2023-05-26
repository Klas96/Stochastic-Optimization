import numpy as np
from . import GetNearestNeighbourPathlen, UpdatePheromoneLevels, ComputeDeltaPheromoneLevels


class AS():
    """
    Ant system (AS) for Traveling Sales Man Problem (TSP)
    Optimization Algorithm for solving the traveling sales man problem.
    """

    def __init__(self, cityLocation):
        self.nodes = cityLocation

        numberOfCities = len(self.nodes)

        # Parameters    
        numberOfAnts = 50  # To do: Set to appropriate value.
        alpha = 1.0        # To do: Set to appropriate value.
        beta = 2.0         # To do: Set to appropriate value.
        rho = 0.7          # To do: set to appropriate value.

        # To do: Write the GetNearestNeighbourPathlen function
        nearestNeighbourPathlen = GetNearestNeighbourPathlen(self.nodes)
        tau0 = numberOfAnts/nearestNeighbourPathlen


        range = [0, 20, 0, 20]

    def run(targetPathlen):

        minimumPathlen = float('infinity')
        iIteration = 0

        # Main loop
        while (minimumPathlen > targetPathlen):
            iIteration = iIteration + 1

            # Generate paths:

            pathCollection = []
            pathlenCollection = []
            for k in range(1, numberOfAnts):
                path = GeneratePath(pheromoneLevel, visibility, alpha, beta)
                pathlen = get_path_len(path, cityLocation)
                if (pathlen < minimumPathlen):
                    minimumPathlen = pathlen
                    minimum = path
                    print(f"Iteration {iIteration}, ant {k}: path len = {minimumPathlen}")
                    PlotPath(connection, cityLocation,path)
                pathCollection = pathCollection.append(path)

        pathlenCollection = pathlenCollection.append(pathlen)

        # Update pheromone levels
        #breakpoint()

        deltaPheromoneLevel = ComputeDeltaPheromoneLevels(pathCollection,pathlenCollection)
        pheromoneLevel = UpdatePheromoneLevels(pheromoneLevel,deltaPheromoneLevel,rho)
        
        PlotPath(connection,cityLocation,minimum)
        title(['Traversions: ' num2str(iIteration) ' len: ' num2str(minimumPathlen)])


def ChoosePath(phermoneArray, visibilityArray, alpha, beta, tabuList):
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