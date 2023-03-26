import numpy as np
import pandas as pd

class particle():
    """
    Particel for searching solution to a problem

    #TODO make N dimensional
    """

    def __init__(self):
        self.pos = (0, 0)
        self.vel = (0, 0)
        self.optima = None
        
    def move(self):
        self.pos += self.vel

    def upadte_velocity(self, optima, max_velocity):
        """
        aimes the particel towards optima
        """

        # Restricting Velocities
        # Cap the value from below
        value = max(self, min_value)

        # Cap the value from above
        value = min(value, max_value)

    def upadte_value(self, objective_function):
        self.value = objective_function(*self.pos)
        if self.value < self.optima:
            self.optima = self.value()
        
        return self.optima





def initialize_swarm(swarm_size, itervall):
    """
    Initilizes Swarm particels
    
    Args:
    
    Returns:
        df with swarm
    """

    cols = ['Position', 'Velocity', 'BestPosition', 'BestValue']

    swarm = pd.DataFrame(np.random.uniform(*itervall, size=(swarm_size, 4)), columns=cols)

    return swarm