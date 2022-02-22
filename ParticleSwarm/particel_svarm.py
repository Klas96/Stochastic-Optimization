import numpy as np
import pandas as pd

from particle import initialize_swarm

def main():

  ret = PSO()
  print(ret)


def PSO(swarm_size=50, itervall = [-5, 5]):
  """
  Args:
    swarm_size -
    itervall -

  Returns:
  
  """
  
  particle_swarm = initialize_swarm(swarm_size, itervall)

  minima = LetTheSwarmStorm(particle_swarm)

  return(minima)

def LetTheSwarmStorm(particel_swarm, time=1, inertiaConst = 1.4):
  """
  """
    
  best_found_particel = particel_swarm[1]
  swarm_min = particel_swarm[1]

  iter = 0
  while(best_found_particel(5) > 0.0001):
    iter = iter + 1
    inertiaConst = inertiaConst*0.99
    if(inertiaConst < 0.35):
      inertiaConst = 0.35

      particle_swarm, swarm_min = move_swarm(particel_swarm)

    if(swarm_min(5) < best_found_particel(5)):
      best_found_particel = swarm_min
      print("Iteration {iter}")
      print("New Best X,Y")
      print([best_found_particel(5), best_found_particel(1), best_found_particel(2)])

    particle_swarm = update_swarms_best(particle_swarm,best_found_particel,inertiaConst)
    theminimaOfthaMinimima = best_found_particel

    return(theminimaOfthaMinimima)


def move_swarm(particel_swarm):
  """
  Moves Swarm and gives Swarm min

  Args:

  Returns:

  """

  swarm_min = float('inf')
  for particle in particel_swarm:
    particle['pos'] = particle['pos'] + particle['vel']

    if particle['value'] <  swarm_min:
       swarm_min = particle['value']

  return(particel_swarm, swarm_min)

def update_swarms_best(particle_swarm,swarmBest,inertiaConst, cognetive_const = 2, social_const = 2):
  timeStep = 1
  vMax = 3/5

  for particel in particle_swarm:
    particle_best_point = particel['BestPoint']
    xSwarmBest = swarmBest(6)
    ySwarmBest = swarmBest(7)

    # Cognetive_const
    accelerartion = np.random.uniform(0,1)*cognetive_const*(particle_best_point-particle_swarm['position'])

    # social_const
    accelerartion += np.random.uniform(0,1)*social_const*(xSwarmBest-particle_swarm['position'])

    # InertiaConst
    accelX = accelX + inertiaConst*particel['velocity']

    particel['acceleration'] = accelerartion

    # Restricting Velocities
    if(abs(particel['velocity']) > vMax):
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
