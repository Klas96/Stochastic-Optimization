function Main()
    AS()
end

%Debuging the ant system :3
function DeBug()
    %AS()
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Parameters
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    numberOfAnts = 50;  % To do: Set to appropriate value.
    alpha = 1.0;        % To do: Set to appropriate value.
    beta = 2.0;         % To do: Set to appropriate value.
    rho = 0.7;          % To do: set to appropriate value.

    addpath('./TSPgraphics');

    cityLocation = LoadCityLocations();
    numberOfCities = length(cityLocation);
    nearestNeighbourPathLength = GetNearestNeighbourPathLength(cityLocation);
    tau0 = numberOfAnts/nearestNeighbourPathLength;
    pheromoneLevel = InitializePheromoneLevels(numberOfCities, tau0);
    visibility = GetVisibility(cityLocation);

    path = GeneratePath(pheromoneLevel, visibility, alpha, beta)
    GetPathLength(path,cityLocation)
    GetPathLength(randperm(50),cityLocation)
    GetPathLength(randperm(50),cityLocation)
    GetPathLength(randperm(50),cityLocation)

end
function AS()
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % Ant system (AS) for TSP.
    %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    clear all;
    clc;
    clf;

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Data
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    addpath('./TSPgraphics');
    cityLocation = LoadCityLocations();
    numberOfCities = length(cityLocation);

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Parameters
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    numberOfAnts = 50;  % To do: Set to appropriate value.
    alpha = 1.0;        % To do: Set to appropriate value.
    beta = 2.0;         % To do: Set to appropriate value.
    rho = 0.7;          % To do: set to appropriate value.

    % To do: Write the GetNearestNeighbourPathLength function
    nearestNeighbourPathLength = GetNearestNeighbourPathLength(cityLocation);
    tau0 = numberOfAnts/nearestNeighbourPathLength;

    targetPathLength = 123.0;
    targetPathLength = 124.0;
    targetPathLength = 125.0;
    targetPathLength = 125.5;
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Initialization
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    range = [0 20 0 20];
    tspFigure = InitializeTspPlot(cityLocation, range);
    connection = InitializeConnections(cityLocation);

    pheromoneLevel = InitializePheromoneLevels(numberOfCities, tau0);
    visibility = GetVisibility(cityLocation);

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Main loop
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    minimumPathLength = inf;

    iIteration = 0;

    while (minimumPathLength > targetPathLength)
     iIteration = iIteration + 1;

     %%%%%%%%%%%%%%%%%%%%%%%%%%
     % Generate paths:
     %%%%%%%%%%%%%%%%%%%%%%%%%%

     pathCollection = [];
     pathLengthCollection = [];
     for k = 1:numberOfAnts
      path = GeneratePath(pheromoneLevel, visibility, alpha, beta);
      pathLength = GetPathLength(path,cityLocation);
      if (pathLength < minimumPathLength)
        minimumPathLength = pathLength;
        minimum = path
        disp(sprintf('Iteration %d, ant %d: path length = %.5f',iIteration,k,minimumPathLength));
        PlotPath(connection,cityLocation,path);
      end
      pathCollection = [pathCollection; path];

      pathLengthCollection = [pathLengthCollection; pathLength];
     end

     %%%%%%%%%%%%%%%%%%%%%%%%%%
     % Update pheromone levels
     %%%%%%%%%%%%%%%%%%%%%%%%%%

     deltaPheromoneLevel = ComputeDeltaPheromoneLevels(pathCollection,pathLengthCollection);
     pheromoneLevel = UpdatePheromoneLevels(pheromoneLevel,deltaPheromoneLevel,rho);

    end
    
    PlotPath(connection,cityLocation,minimum);
    title(['Traversions: ' num2str(iIteration) ' Length: ' num2str(minimumPathLength)])
end

%Pre:
  %pheromoneLevel: levels of phermone at eveary path
  %deltaPheromoneLevel:
  %rho:
%Ret:
  %pheromoneLevel: New and updated phermone levles
%TestStaus: None
%Dependencies:
function pheromoneLevel = UpdatePheromoneLevels(pheromoneLevel,deltaPheromoneLevel,rho)
  pheromoneLevel = pheromoneLevel.*(1-rho) + deltaPheromoneLevel;

end

%Pre:
  %pathCollection: A collection of all paths
  %pathLengthCollection: A colection of all path Lengths
%Ret
  %Matrix ofpathCollection the Phermone Updat levels decide py the path
function deltaPheromoneLevel = ComputeDeltaPheromoneLevels(pathCollection,pathLengthCollection)
  deltaPheromoneLevel = zeros(length(pathCollection(1,:)),length(pathCollection(1,:)));

  for iPath = 1:length(pathCollection(:,1))
    update = 1/pathLengthCollection(iPath);
    for iCity = 1:(length(pathCollection(1,:))-1)

      fromCity = pathCollection(iPath,iCity);
      toCity = pathCollection(iPath,iCity+1);

      deltaPheromoneLevel(fromCity,toCity) = deltaPheromoneLevel(fromCity,toCity) + update;
      %deltaPheromoneLevel(toCity,fromCity) = deltaPheromoneLevel(toCity,fromCity) + update;
    end
  end
end

%Pre:
  %pheromoneLevel: levels of phermone at eveary path
  %visibility
  %alpha: Const
  %beta: Const
  %tabuList: List of allready vivited Nodes
%Ret:
  %path: Path generated
%TestStaus: OK
%Dependencies: ChoosePath
%Problem Kommer gå från sig själv till sig själv hela tiden??
function path = GeneratePath(pheromoneLevel, visibility, alpha, beta)

  indexForCitys = 1:length(pheromoneLevel);
  %tabuList = true(1,length(pheromoneLevel(:,1)));
  %cityIndexList = 1:length(pheromoneLevel(:,1));
  startingPoint = randi(length(pheromoneLevel(1,:)));
  path = [startingPoint];

  for i = 1:(length(pheromoneLevel(1,:))-1)

    %tabuList(startingPoint) = false;
    %Take This one
    phermoneArray = pheromoneLevel(startingPoint,:);
    phermoneArray(startingPoint) = [];
    visibilityArray = visibility(startingPoint,:);
    visibilityArray(startingPoint) = [];
    %Remove
    pheromoneLevel(startingPoint,:) = [];
    pheromoneLevel(:,startingPoint) = [];
    visibility(startingPoint,:) = [];
    visibility(:,startingPoint) = [];
    indexForCitys(startingPoint) = [];
    nextCity = ChoosePath(phermoneArray, visibilityArray, alpha, beta);

    path = [path indexForCitys(nextCity)];
    startingPoint = nextCity;
  end
end

%Pre:
  %startingPoint
  %pheromoneLevel: levels of phermone at eveary path
  %visibility
  %alpha: Const
  %beta: Const
  %tabuList: Boulean list. Faslse - visited
%Ret:
  %nextVeretex: Next Veretex chosen
%TestStaus: OK
%Dependencies: RunChoise
function nextVeretex = ChoosePath(phermoneArray, visibilityArray, alpha, beta,tabuList)
  nextVeretex = RunChoise(phermoneArray,visibilityArray,alpha, beta);
end

%Ändra
%Pre:
  %startingPoint
  %tabuFreePhermone: Phermone Levels where the tabu poistions have been removed
  %tabuFreeVisibility: visibility where the tabu poistions have been removed
  %alpha: Const
  %beta: Const
%Ret:
  %indexChosen: The index chosen
%TestStaus: OK
%Dependencies: None
function indexChosen = RunChoise(phermoneArray,visibilityArray,alpha, beta)
  r = rand;
  probLow = 0;
  probHigh = 0;
  indexChosen = 1;

  %Making Normalizing Factor
  normlize = phermoneArray.^alpha;
  normlize = sum(normlize.*visibilityArray.^beta);

  %Loop Through the allowed cities
  for i = 1:length(phermoneArray)
    probInter = phermoneArray(i).^alpha;
    probInter = probInter.*visibilityArray(i).^beta;
    probInter = probInter./normlize;

    probHigh = probLow + probInter;
    if probLow <= r && r <= probHigh
      indexChosen = i;
    end
    probLow = probHigh;
  end
end

%Pre:
%numberOfCities:
  %tau0: Starting phermone
%Ret:
  %pheromoneLevel: Matrix of Paths With starting Phermone.
%TestStaus: None
%Dependencies: None
function pheromoneLevel = InitializePheromoneLevels(numberOfCities, tau0)
  pheromoneLevel(1:numberOfCities,1:numberOfCities) = tau0;
end

%Pre:
  %cityLocation: 2d positions of all avaliable cities
%Ret:
  %nearNeigPathLen: Length Of The Nearest Naigbhor Path
%TestStaus: None
%Dependencies: GetDist
function visib = GetVisibility(cityLocation)
  numberOfCities = length(cityLocation(:,1));
  visib = zeros(numberOfCities,numberOfCities);

  neaNergLength = 0;
  neaNergIndex = 0;

  for i = 1:length(cityLocation(:,1))
    for j = 1:length(cityLocation)
      if(i ~= j)
        neaNergLength = GetDist(cityLocation(i,:), cityLocation(j,:));
        visib(i,j) = 1/neaNergLength;
      end
    end
  end
end

%Pre:
  %cityLocation: 2d positions of all avaliable cities
  %Path: Path that you want to know the length of
%Ret:
  %pathLen: Length Of The Path
%TestStaus: None
%Dependencies: GetDist
function pathLen = GetPathLength(path,cityLocation)
  pathLen = 0;

  for i = 1:(length(path)-1)
    indexFrom = path(i);
    indexTo = path(i+1);
    possFrom = cityLocation(indexFrom,:);
    possTo = cityLocation(indexTo,:);

    newLen = GetDist(possFrom,possTo);
    pathLen = pathLen + newLen;
  end

  possFrom = cityLocation(path(end),:);
  possTo = cityLocation(path(1),:);
  newLen = GetDist(possFrom,possTo);

  pathLen = pathLen + newLen;

end

%Pre:
%cityLocation: 2d positions of all avaliable cities
%ret
%nearNeigPathLen: Length Of The Nearest Naigbhor Path
%TestStaus: None
%Dependencies: GetNearestNeighbour
function nearNeigPathLen = GetNearestNeighbourPathLength(cityLocation)

  nearNeigPathLen = 0;
  lengthNearestTot = 0;
  neaNergIndex = randi(length(cityLocation(:,1)));
  firstCityPos = cityLocation(neaNergIndex,:);
  for cityIndex = 1:(length(cityLocation(:,1))-1)
    cityPos = cityLocation(neaNergIndex,:);
    cityLocation(neaNergIndex,:) = [];
    [neaNergLength neaNergIndex] = GetNearestNeighbour(cityPos, cityLocation);
    lengthNearestTot = lengthNearestTot + neaNergLength;
  end

  %Conect
  dist = GetDist(cityPos, firstCityPos);
  lengthNearestTot = lengthNearestTot + neaNergLength;

  nearNeigPathLen = lengthNearestTot;

end

%Pre 2d pos cityPos, array of 2d pos cityLocations
%ret index of nearest path, lengthNearest path
%TestStaus: None
%Dependencies: GetDist
function [neaNergLength neaNergIndex] = GetNearestNeighbour(cityPos, cityLocations)

  indexNearest = 0;

  distMin = inf;
  for i = 1:(length(cityLocations(:,1)))
    dist = GetDist(cityPos, cityLocations(i,:));
    if(dist < distMin)
      distMin = dist;
      indexNearest = i;
    end
  end

  neaNergIndex = indexNearest;
  neaNergLength = distMin;
end

%Pre 2d pos cityPos, array of 2d pos cityLocations
%pos1,pos2: 2d positions
%ret distance Between positions
%TestStaus: None
%Dependencies: None
function dist = GetDist(pos1,pos2)
  %X Pos
  xDiff = pos1(1) - pos2(1);
  %Y Pos
  yDiff = pos1(2) - pos2(2);

  dist = sqrt(xDiff.^2 + yDiff.^2);
end