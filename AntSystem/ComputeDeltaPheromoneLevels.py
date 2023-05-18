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
