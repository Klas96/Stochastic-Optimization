import numpy as np

# Main
def main():

  CountorPlot()
  #hold on
  #saveas(gcf,'CountorPlot','epsc')

  svar = PSO()

  print("Minima was found as \n")
  print(f"X = {svar(6)}")
  print(f"Y = {svar(7)}")
  print(f"f = {svar(5)}")


def CountorPlot():
  x = np.linspace(-5,5)
  y = np.linspace(-5,5)
  [X,Y] = meshgrid(x,y)

  Z = log(GetFunctionVal(X,Y))

  contourf(X,Y,Z)


def PSO(swarm_size=50, itervall = [-5, 5]):
  """
  Args:
    swarm_size -
    itervall -
  Returns:
  
  """
  
  particelSwarm = initialize_swarm(swarm_size, itervall)

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

      particelSwarm, swarmMin = move_swarm(particelSwarm)

      if(swarmMin(5) < bestFoundParticel(5)):
        bestFoundParticel = swarmMin
        print("Iteration")
        print(iter)
        print("New Best X,Y")
        print([bestFoundParticel(5), bestFoundParticel(1), bestFoundParticel(2)])


      particelSwarm = update_swarms_best(particelSwarm,bestFoundParticel,inertiaConst)

    theminimaOfthaMinimima = bestFoundParticel
    plot_part_swarm(particelSwarm)
    #title(["Iteration " num2str(iter)])
    return(theminimaOfthaMinimima)


def plot_part_swarm(particelSwarm):
  #CountorPlot()
  for i in range(1,len(particelSwarm(:,1))):
    xIndi = particelSwarm(i,1)
    yIndi = particelSwarm(i,2)
    u = particelSwarm(i,3)
    v = particelSwarm(i,4)
    quiver(xIndi,yIndi,u,v,'b')


# Moves Swarm and gives Swarm min
def move_swarm(particelSwarm):
  swarmMin = particelSwarm[1,:]
  for i in range(1:len(particelSwarm(:,1))):
    particelSwarm(i, 1) = particelSwarm(i, 1) + particelSwarm(i, 3)
    particelSwarm(i, 2) = particelSwarm(i, 2) + particelSwarm(i, 4)

    if particelSwarm(i,5) <  swarmMin(5):
       swarmMin = particelSwarm[i,:]

  return(particelSwarm, swarmMin)

def update_swarms_best(particelSwarm,swarmBest,inertiaConst):
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

    particel_swarm(i,3) = accelX
    particel_swarm(i,4) = accelY

    # Restricting Velocities
    if(abs(particel_swarm(i,3)) > vMax):
      if(particel_swarm(i,3) < 0):
        particel_swarm(i,3) = -vMax


      if(particel_swarm(i,3) > 0):
        particel_swarm(i,3) = vMax


    if(abs(particel_swarm(i,4)) > vMax):
      if(particel_swarm(i,4) < 0):
        particel_swarm(i,4) = -vMax
      elif(particel_swarm(i,4) > 0):
        particel_swarm(i,4) = vMax


    xIndi = particel_swarm(i,1)
    yIndi = particel_swarm(i,2)
    func = get_function_val(xIndi,yIndi)

    if func <  particelSwarm(i,5):
      particel_swarm(i,5) = func
      particel_swarm(i,6) = xIndi
      particel_swarm(i,7) = yIndi

  return(particel_swarm)


def get_funtion_val(x,y):
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

    print('\nFinding Median ')
    UpdateProgressbar(medianMeter)


  if(gaProg>=0):
    gaMeter = gaProg

    print('\nRunning PSO     ')
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