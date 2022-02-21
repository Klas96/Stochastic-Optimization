import numpy as np
import pandas as pd


def main():

  CountorPlot()

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
  
  particle_swarm = initialize_swarm(swarm_size, itervall)

  minima = LetTheSwarmStorm(time, particle_swarm)

  return(minima)

def LetTheSwarmStorm(time, particel_swarm, inertiaConst = 1.4):
  """
  """
    
  bestFoundParticel = particel_swarm(1,:)
  swarmMin = particel_swarm(1,:)

  iter = 0
  while(bestFoundParticel(5) > 0.0001):
    iter = iter + 1
    inertiaConst = inertiaConst*0.99
    if(inertiaConst < 0.35):
      inertiaConst = 0.35

      particle_swarm, swarmMin = move_swarm(particel_swarm)

    if(swarmMin(5) < bestFoundParticel(5)):
      bestFoundParticel = swarmMin
      print("Iteration {iter}")
      print("New Best X,Y")
      print([bestFoundParticel(5), bestFoundParticel(1), bestFoundParticel(2)])


    particle_swarm = update_swarms_best(particle_swarm,bestFoundParticel,inertiaConst)

    theminimaOfthaMinimima = bestFoundParticel
    plot_part_swarm(particle_swarm)
    return(theminimaOfthaMinimima)


def plot_part_swarm(particle_swarm):
  """
  """
  #CountorPlot()
  for i in range(1,len(particle_swarm(:,1))):
    xIndi = particle_swarm(i,1)
    yIndi = particle_swarm(i,2)
    u = particle_swarm(i,3)
    v = particle_swarm(i,4)
    quiver(xIndi,yIndi,u,v,'b')


# Moves Swarm and gives Swarm min
def move_swarm(particel_swarm):
  """
  """
  swarmMin = particel_swarm[1,:]
  for i in range(1:len(particle_swarm(:,1))):
    particle_swarm(i, 1) = particle_swarm(i, 1) + particle_swarm(i, 3)
    particle_swarm(i, 2) = particle_swarm(i, 2) + particle_swarm(i, 4)

    if particle_swarm(i,5) <  swarmMin(5):
       swarmMin = particle_swarm[i,:]

  return(particle_swarm, swarmMin)

def update_swarms_best(particle_swarm,swarmBest,inertiaConst, cognetive_const = 2, social_const = 2):
  timeStep = 1
  vMax = 3/5

  for i in range(1, len(particle_swarm(:,1))):
    xPartBest = particle_swarm(i, 6)
    yPartBest = particle_swarm(i, 7)
    xSwarmBest = swarmBest(6)
    ySwarmBest = swarmBest(7)

    accelX = 0
    accelY = 0

    # Cognetive_const
    accelX = accelX + cognetive_const*rand*(xPartBest-particle_swarm(i,1))
    accelY = accelY + cognetive_const*rand*(yPartBest-particle_swarm(i,2))

    # social_const
    accelX = accelX + social_const*rand*(xSwarmBest-particle_swarm(i,1))
    accelY = accelY + social_const*rand*(ySwarmBest-particle_swarm(i,2))

    # InertiaConst
    accelX = accelX + inertiaConst*particle_swarm(i,3)
    accelY = accelY + inertiaConst*particle_swarm(i,4)

    particel_swarm[i,3] = accelX
    particel_swarm[i,4] = accelY

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

    if func <  particle_swarm(i,5):
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