# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# make array of all susceptible population
population = np.zeros((100, 100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# define the basic variables of the model
beta = 0.3
gamma = 0.05
time_steps = 100

'''
For the simulation:
1. Find all currently infected persons
2. For each infected cell, try to infect its 8 neighboring persons with probability beta
3. Allow infected persons to recover with probability gamma
4. Update the population grid and visualize
'''

# Prepare for visualization
time_points = [0, 10, 50, 100]
shot = []
shot.append(population.copy())

# Run the spatial SIR simulation
for step in range(time_steps):
    new_population = population.copy()
    infected_y, infected_x = np.where(population == 1)
    for y, x in zip(infected_y, infected_x):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                # Neighbor infection
                ny = y + dy
                nx = x + dx
                if 0 <= ny < 100 and 0 <= nx < 100:
                    if population[ny, nx] == 0:
                        if np.random.random() < beta:
                            new_population[ny, nx] = 1
                # Recovery
                if dy == 0 and dx == 0:
                    if np.random.random() < gamma:
                        new_population[y, x] = 2

    # data entry
    population = new_population
    if (step + 1) in time_points:
        shot.append(population.copy())

#plot the result
fig, axes = plt.subplots(2, 2, figsize=(6, 4), dpi=150)
axes = axes.flatten()
idx = 0
for t in time_points:
    im = axes[idx].imshow(shot[idx], cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
    axes[idx].set_title(f'Time step = {t}')
    idx += 1
plt.tight_layout()
plt.savefig("spatial_SIR_evolution.png", dpi=300)
plt.show()