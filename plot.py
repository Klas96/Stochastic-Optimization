import numpy as np
import matplotlib.pyplot as plt

def CountorPlot():
    """
    Generate a contour plot.
    """
    # Create sample data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    Z = np.sin(np.sqrt(X**2 + Y**2))

    # Create contour plot
    plt.contourf(X, Y, Z, cmap='coolwarm')
    plt.colorbar()

    # Add labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Contour Plot')

    # Show plot
    plt.show()

def plot_part_swarm(particle_swarm):
  """
  Plot the particle 
  """
  #CountorPlot()
  for particel in particle_swarm.particles:
    x_pos = particel.pos[0]
    y_pos = particel.pos[1]

    x_vel = x_pos + particel.vel[0]
    y_vel = y_pos + particel.pos[1]
    
    fig, ax = plt.scatter(x_pos, y_pos, 'x')

    ax.arrow(x_pos, y_pos, x_vel, y_vel)
