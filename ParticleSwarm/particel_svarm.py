# Main
def main():

  CountorPlot()
  #hold on
  #saveas(gcf,'CountorPlot','epsc')

  svar = PSO()

  print("Minima was found as \n")
  print("X = ")
  print(svar(6))
  print("  Y = ")
  print(svar(7))
  print("  f = ")
  print(svar(5))

  plot(svar(6), svar(7), 'yo')


def CountorPlot():
  x = linspace(-5,5)
  y = linspace(-5,5)
  [X,Y] = meshgrid(x,y)

  Z = log(GetFunctionVal(X,Y))

  contourf(X,Y,Z)


def PSO():
  time = 1000000
  swarmSize = 50
  itervall = [-5, 5]

  #X Y vX vY indiBest xIndiBest yIndiBest
  particelSwarm = InitializeSwarm(swarmSize, itervall)

  theminimaOfthaMinimima = LetTheSwarmStorm(time, particelSwarm)
  print("Best Found Minima")
  print(theminimaOfthaMinimima)
  return(theminimaOfthaMinimima)

def LetTheSwarmStorm(time,particelSwarm):
    inertiaConst = 1.4
    bestFoundParticel = particelSwarm(1,:)
    swarmMin = particelSwarm(1,:)

    iter = 0
    while(bestFoundParticel(5) > 0.0001):
      iter = iter + 1

      inertiaConst = inertiaConst*0.99
      if(inertiaConst < 0.35):
        inertiaConst = 0.35

      [particelSwarm swarmMin] = MoveSwarm(particelSwarm)

      if(swarmMin(5) < bestFoundParticel(5))
        bestFoundParticel = swarmMin
        disp("Iteration")
        disp(iter)
        disp("New Best X,Y")
        disp([bestFoundParticel(5) bestFoundParticel(1) bestFoundParticel(2)])


      particelSwarm = UpdateSwarmsBest(particelSwarm,bestFoundParticel,inertiaConst)
      #UpdateDisp(-1,i./time.*100,-1)

    theminimaOfthaMinimima = bestFoundParticel
    plotPartSwarm(particelSwarm)
    #title(["Iteration " num2str(iter)])
    return(theminimaOfthaMinimima)


def plotPartSwarm(particelSwarm):
  #CountorPlot()
  for i = 1:length(particelSwarm(:,1)):
    xIndi = particelSwarm(i,1)
    yIndi = particelSwarm(i,2)
    plot(xIndi,yIndi,'rx')
    u = particelSwarm(i,3)
    v = particelSwarm(i,4)
    quiver(xIndi,yIndi,u,v,'b')


# Moves Swarm and gives Swarm min
def MoveSwarm(particelSwarm):
  swarmMin = particelSwarm(1,:)
  for i in range(1:len(particelSwarm(:,1))):
    particelSwarm(i, 1) = particelSwarm(i, 1) + particelSwarm(i, 3)
    particelSwarm(i, 2) = particelSwarm(i, 2) + particelSwarm(i, 4)

    if particelSwarm(i,5) <  swarmMin(5)
       swarmMin = particelSwarm(i,:)

  return(particelSwarm, swarmMin)


# Updates Velocities And ParticelBest Value and Cordinates
def UpdateSwarmsBest(particelSwarm,swarmBest,inertiaConst):
  timeStep = 1
  cognetiveConst = 2
  socialConst = 2
  vMax = 3/5

  for i in range(1, len(particelSwarm(:,1))):

    xPartBest = particelSwarm(i, 6)
    yPartBest = particelSwarm(i, 7)
    xSwarmBest = swarmBest(6)
    ySwarmBest = swarmBest(7)

    accelX = 0
    accelY = 0

    # CognetiveConst
    accelX = accelX + cognetiveConst*rand*(xPartBest-particelSwarm(i,1))
    accelY = accelY + cognetiveConst*rand*(yPartBest-particelSwarm(i,2))

    # socialConst
    accelX = accelX + socialConst*rand*(xSwarmBest-particelSwarm(i,1))
    accelY = accelY + socialConst*rand*(ySwarmBest-particelSwarm(i,2))

    # InertiaConst
    accelX = accelX + inertiaConst*particelSwarm(i,3)
    accelY = accelY + inertiaConst*particelSwarm(i,4)

    particelSwarm(i,3) = accelX
    particelSwarm(i,4) = accelY

    # Restricting Velocities
    if(abs(particelSwarm(i,3)) > vMax)
      if(particelSwarm(i,3) < 0):
        particelSwarm(i,3) = -vMax


      if(particelSwarm(i,3) > 0):
        particelSwarm(i,3) = vMax


    if(abs(particelSwarm(i,4)) > vMax):
      if(particelSwarm(i,4) < 0):
        particelSwarm(i,4) = -vMax
      elif(particelSwarm(i,4) > 0):
        particelSwarm(i,4) = vMax


    xIndi = particelSwarm(i,1)
    yIndi = particelSwarm(i,2)
    func = GetFunctionVal(xIndi,yIndi)

    if func <  particelSwarm(i,5):
      particelSwarm(i,5) = func
      particelSwarm(i,6) = xIndi
      particelSwarm(i,7) = yIndi

  return(particelSwarm)


def GetFunctionVal(x,y):
  #f (x, y) = (x 2 + y − 11) 2 + (x + y 2 − 7) 2 , (x, y) ∈ [−5, 5]
  funcVal = (x**2 + y - 11)**2 + (x + y**2-7)**2
  #funcVal = log(funcVal)
  return(funcVal)



# Estetics
def UpdateDisp(meidanProg, gaProg, pMutaionValue):
  #persistent medianMeter
  #persistent gaMeter
  #persistent mutMeter
  
  if(meidanProg>=0):
    medianMeter = meidanProg

    fprintf('\nFinding Median ')
    UpdateProgressbar(medianMeter)


  if(gaProg>=0):
    gaMeter = gaProg

    fprintf('\nRunning PSO     ')
    UpdateProgressbar(gaMeter)
  return(noOut)


def UpdateProgressbar(c):
  # Vizualization parameters

  strPercentageLength = 20
  strDotsMaximum      = 20

  # Progress bar - normal progress
  c = floor(c)
  percentageOut = [num2str(c) '%%']
  percentageOut = [percentageOut repmat(' ',1,strPercentageLength-length(percentageOut)-1)]
  nDots = floor(c/100*strDotsMaximum)
  dotOut = ['[' repmat('>',1,nDots) repmat(' ',1,strDotsMaximum-nDots) ']']
  strOut = [percentageOut dotOut]

  print([strOut])