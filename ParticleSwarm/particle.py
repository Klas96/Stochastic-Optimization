import numpy as np

class particle():

    def __init__(self):
        self.pos = (0, 0)
        self.vel = (0, 0)

    def move(self):
        self.pos += self.vel


def initialize_swarm(swarm_size, itervall):
    """
    Initilizes Swarm particels
    Returns - df with swarm
    """
    cols = ['Position', 'Velocity', 'BestPosition', 'BestValue']

    swarm = pd.DataFrame(np.random(), columns=cols)

    return swarm 