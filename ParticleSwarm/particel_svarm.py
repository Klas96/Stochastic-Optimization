import numpy as np
import pandas as pd
from particle import initialize_swarm
from target_function import get_funtion_val
import particle


class ParticleSwarm():

  def __init__(self) -> None:
    NumberOfParticles = 50
    dimensions = 2

    self.particel_list = []
    #init numer of particels
    for i in range(self.NumberOfParticles):
      self.particel_list.append(particle())

    self.swarm_optimal_value = None
    self.swarm_optimal_varibales = None
    self.velocity_max = 3/5
    self.timeStep = 1
    self.cognetive_const = 2
    self.social_const = 2

  def move_swarm(self):
    """
    Moves Swarm and gives Swarm min

    Args:

    Returns:
    """

    swarm_min = float('inf')
    for particle in self.particel_list:
      particle.move()

  def update_swarm_direction(self):
    """
    Update the velocity of the particels
    """
    for particle in self.particel_list:
      particle.aim(self.swarm_optimal_value)

  def update_swarm_values(self, objective_func):
    #Update Partikels
    for particel in self.particel_list:
      particel_value = particel.upadte_value(objective_func)

      #Treating Optimization as minimazation problem
      if particel_value < self.swarm_optimal_value:
        self.swarm_optimal_value = particel_value
        
  def run_optimization(self, objective_func):
    """
    Optimize objective function
    """

    for epoch in range(100):
      self.move_swarm()
      self.update_swarm_values()
      self.update_swarm_direction()

    return(self.swarm_optimal_varibales, self.swarm_optimal_value)

if __name__ == '__main__':
  ret = PSO()
  print(ret)
