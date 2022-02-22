import numpy as np
import pandas as pd

class particle():

    def __init__(self):
        self.pos = (0, 0)
        self.vel = (0, 0)

    def move(self):
        self.pos += self.vel


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