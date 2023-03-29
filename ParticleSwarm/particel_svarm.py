import numpy as np
import pandas as pd
from ParticleSwarm.particle import particle


class ParticleSwarm():

  def __init__(self, lower_bound, upper_bound, max_vel) -> None:
    self.number_of_particles = 50
    dimensions = 2

    self.particel_list = []
    #init numer of particels
    for i in range(self.number_of_particles):
      self.particel_list.append(particle(lower_bound, upper_bound))

    self.swarm_optimal_value = float('inf')
    self.swarm_optimal_varibales = None
    self.velocity_max = max_vel
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


  def update_swarm_veloceties(self):
    """
    Update the velocity of the particels
    """
    for particle in self.particel_list:
      particle.upadte_velocity(self.swarm_optimal_value, self.velocity_max)


  def update_swarm_values(self, objective_func):
    #Update Partikels
    for particel in self.particel_list:
      particel_value = particel.upadte_value(objective_func)

      #Treating Optimization as minimazation problem
      if particel_value < self.swarm_optimal_value:
        self.swarm_optimal_value = particel_value
        self.swarm_optimal_varibales = particel.varibale_optima
  

  def run_optimization(self, objective_func, epochs=100):
    """
    Optimize objective function
    """

    for epoch in range(epochs):
      self.move_swarm()
      self.update_swarm_values(objective_func)
      self.update_swarm_direction()

    return(self.swarm_optimal_varibales, self.swarm_optimal_value)

if __name__ == '__main__':
  ret = ParticleSwarm()
  print(ret)
