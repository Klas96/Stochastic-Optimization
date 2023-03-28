import numpy as np
import pandas as pd
import math

class particle():
    """
    Particel for searching solution to a problem

    #TODO make N dimensional
    """

    def __init__(self, lower_bound, upper_bound, n=2):
        """
        Initilizes Position and Velocity of the particle.
        """
        self.pos = np.random.uniform(lower_bound, upper_bound, size=(n,))
        vel_bound = upper_bound - lower_bound
        self.vel = np.random.uniform(-vel_bound, vel_bound, size=(n,))
        self.optima = float('inf')
        self.varibale_optima = None
        
    def move(self):
        self.pos += self.vel

    def upadte_velocity(self, optima,
                        max_velocity,
                        inertia_constant = 0.7,
                        cognetuive_constant = 2,
                        social_constant = 2):
        """
        aimes the particel towards optima acording to
        vi,d ← w vi,d + φp rp (pi,d-xi,d) + φg rg (gd-xi,d)
        """

        #np.random.uniform(0,1)
        self.vel = (inertia_constant*self.vel[0], inertia_constant*self.vel[1])

        # Cognative constant
        rand = np.random.uniform(0,1)
        self.vel = (self.vel[0] + rand*cognetuive_constant*self.vel[0], self.vel[1] + rand*cognetuive_constant*self.vel[1])

        # Social Constant
        rand = np.random.uniform(0,1)
        self.vel = (self.vel[0] + rand*social_constant*self.vel[0], self.vel[1] + rand*social_constant*self.vel[1])

        # Cap the value from above
        magnitude = math.sqrt(self.vel[0]**2 + self.vel[1]**2)
     
        if magnitude > max_velocity:
            # Calculate the scaling factor to preserve the direction of the vector
            scale_factor = max_velocity/magnitude

            # Scale down the vector components
            self.vel = (self.vel[0]*scale_factor, self.vel[1]*scale_factor)

    def upadte_value(self, objective_function):
        """
        Update the value of the particle
        """

        self.value = objective_function(*self.pos)
        
        if self.value < self.optima:
            self.optima = self.value
            self.varibale_optima = self.pos
        
        return self.optima


"""
def initialize_swarm(swarm_size, itervall):
    ""
    Initilizes Swarm particels
    
    Args:
    
    Returns:
        df with swarm
    ""

    cols = ['Position', 'Velocity', 'BestPosition', 'BestValue']

    swarm = pd.DataFrame(np.random.uniform(*itervall, size=(swarm_size, 4)), columns=cols)

    return swarm
"""