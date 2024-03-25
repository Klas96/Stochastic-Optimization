import numpy as np
import matplotlib.pyplot as plt
from particle_swarm import ParticleSwarm
from genetic_algorithm import GA
from genetic_algorithm.decode_chromosone import decode_binary_chromosone
from matplotlib import animation


# Plotting prepartion
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

population_len = 100
#minimum x=7 y=4
objective_func = lambda x,y: (x-7)**2 + (y-4)**2
position_min = 0
position_max = 10

x = np.linspace(position_min, position_max, 80)
y = np.linspace(position_min, position_max, 80)
X, Y = np.meshgrid(x, y)
Z= objective_func(X,Y)
ax.plot_wireframe(X, Y, Z, color='r', linewidth=0.2)
images = []

#optimization_method = 'particle_swarm_pptimization'
optimization_method = 'genetic_algorithm'
if optimization_method == 'particle_swarm_pptimization':
    ps = ParticleSwarm(position_min,
                       position_max,
                       number_of_particles=population_len,
                       cognetive_constant=1,
                       social_constant=1,
                       inetria_constant=0.3,
                       max_vel=0.5)
    particles = []
    for i in range(100):
        image = ax.scatter3D([ps.particel_list[n].pos[0] for n in range(population_len)],
                            [ps.particel_list[n].pos[1] for n in range(population_len)],
                            [objective_func(ps.particel_list[n].pos[0],ps.particel_list[n].pos[1]) for n in range(population_len)], c='b')
        images.append([image])
        ps.run_optimization(objective_func, epochs=1)
        
elif optimization_method == 'genetic_algorithm':
    ga = GA(objective_func, population_size=population_len, init_range = (0,10), verbose=True, numGenerations = 1)

    for i in range(100):
        decoded_var_list = []
        for n in range(population_len):
            decoded_var_list.append(decode_binary_chromosone(ga.population[n], num_var = 2))
            
        image = ax.scatter3D([decoded_var_list[n][0] for n in range(ga.population_size)],
                             [decoded_var_list[n][1] for n in range(ga.population_size)],
                             [objective_func(decoded_var_list[n][0], decoded_var_list[n][1]) for n in range(ga.population_size)], c='b')
        images.append([image])

        curent_optima, all_best_variables = ga.run()
elif optimization_method == 'ant_system':
    pass

# Generate the animation image and save
print("Creating animation")
print("len(images):", len(images))
animated_image = animation.ArtistAnimation(fig, images)
animated_image.save('./'+optimization_method+'.gif', writer='pillow') 