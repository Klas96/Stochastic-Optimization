from ParticleSwarm.particle import Particle


class ParticleSwarm():

  def __init__(self,
               lower_bound,
               upper_bound,
               number_of_particles=50,
               max_vel=2,
               inetria_constant=0.75,
               cognetive_constant=2,
               social_constant=2) -> None:
    self.number_of_particles = number_of_particles
    dimensions = 2
    self.cognetive_const = cognetive_constant
    self.social_const = social_constant
    self.inertia_constant = inetria_constant

    self.particel_list = []
    #init numer of particels
    for i in range(self.number_of_particles):
      self.particel_list.append(Particle(lower_bound, upper_bound))


    self.optimal_particle = self.particel_list[0]
    #self.swarm_optimal_value = float('inf')
    self.swarm_optimal_varibales = self.optimal_particle.pos
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

    for particle in self.particel_list:
      particle.move()


  def update_swarm_direction(self):
    """
    Update the velocity of the particels
    """
    for particle in self.particel_list:
      particle.update_velocity(self.optimal_particle.varibale_optima,
                               self.velocity_max,
                               inertia_constant=self.inertia_constant,
                               cognetuive_constant=self.cognetive_const,
                               social_constant=self.social_const)


  def update_swarm_values(self, objective_func):
    """
    Update the values of the particels and the swarm function values
    """
    #Update Particels
    for particel in self.particel_list:
      particel_value = particel.update_value(objective_func)

      #daglundström

      #Treating Optimization as minimazation problem
      if particel_value < self.optimal_particle.optima:
        #DO I need to do copy here?
        self.optimal_particle = particel
        self.swarm_optimal_varibales = particel.varibale_optima
        print(f"Svarm optima: {self.swarm_optimal_varibales}")


  def run_optimization(self, objective_func, epochs=100):
    """
    Optimize objective function
    """

    for epoch in range(epochs):
      self.move_swarm()
      self.update_swarm_values(objective_func)
      self.update_swarm_direction()

    return(self.swarm_optimal_varibales, self.optimal_particle.optima)