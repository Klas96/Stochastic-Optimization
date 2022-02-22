import numpy as np

def CountorPlot():
  x = np.linspace(-5,5)
  y = np.linspace(-5,5)
  [X,Y] = meshgrid(x,y)

  Z = log(GetFunctionVal(X,Y))

  contourf(X,Y,Z)



def plot_part_swarm(particle_swarm):
  """
  """
  #CountorPlot()
  for particel in particle_swarm:
    xIndi = particle_swarm(i,1)
    yIndi = particle_swarm(i,2)
    u = particle_swarm(i,3)
    v = particle_swarm(i,4)
    quiver(xIndi,yIndi,u,v,'b')