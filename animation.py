import numpy as np
import matplotlib.pyplot as plt
from ParticleSwarm.particel_svarm import ParticleSwarm
from matplotlib import animation


# Plotting prepartion
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

population_len = 50
objective_func = lambda x,y: (x-7)**2 + (y-4)**2
#minimum x=7 y=4
position_min = 0
position_max = 10
ps = ParticleSwarm(position_min, position_max,)
particles = []

x = np.linspace(position_min, position_max, 80)
y = np.linspace(position_min, position_max, 80)
X, Y = np.meshgrid(x, y)
Z= objective_func(X,Y)
ax.plot_wireframe(X, Y, Z, color='r', linewidth=0.2)
images = []

for i in range(100):
    image = ax.scatter3D([ps.particel_list[n].pos[0] for n in range(population_len)],
                         [ps.particel_list[n].pos[1] for n in range(population_len)],
                         [objective_func(ps.particel_list[n].pos[0],ps.particel_list[n].pos[1]) for n in range(population_len)], c='b')
    images.append([image])

    ps.move_swarm()
    ps.update_swarm_values(objective_func)
    ps.update_swarm_direction()

# Generate the animation image and save
animated_image = animation.ArtistAnimation(fig, images)
animated_image.save('./pso_simple.gif', writer='pillow') 