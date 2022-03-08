import numpy as np
import pandas as pd

from particle import initialize_swarm
from target_function import get_funtion_val


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
  Args:

  Returns:

  """
    
  swarm_min_pos = particel_swarm.loc[1]
  swarm_min = float('inf')

  iter = 0
  while(swarm_min > 0.0001):
    iter = iter + 1
    inertiaConst = inertiaConst*0.99
    if(inertiaConst < 0.35):
      inertiaConst = 0.35

    particle_swarm, swarm_move_min = move_swarm(particel_swarm)

    if(swarm_min < swarm_move_min):
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
    if(abs(particel['velocity'][0]) > vMax):
      if(particel['velocity'][0] < 0):
        particel['velocity'][0] = -vMax
      else:
        particel['velocity'][0] = vMax


    if(abs(particel['velocity'][1]) > vMax):
      if(abs(particel['velocity'][1]) < 0):
        particel['velocity'][1] = -vMax 
      else:
        particel['velocity'][1] = vMax

    func = get_funtion_val(particel['pos'])

    if func <  particel['MinValue']:
      particel['MinValue'] = func
      particel['MinPosition'] = particel['pos']

  return(particle_swarm)



if __name__ == '__main__':
  ret = PSO()
  print(ret)