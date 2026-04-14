#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#Create a grid
population = np.zeros((100, 100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

#define the basic variables of the model
beta = 0.3
gamma = 0.05
time_steps = 100

'''
For the simulation:
1. Find all currently infected cells
2. For each infected cell, try to infect its 8 neighboring cells with probability beta
3. Allow infected cells to recover with probability gamma
4. Update the population grid and visualize
'''

# Prepare for visualization
time_points = [0, 10, 50, 100]
snapshots = []
snapshots.append(population.copy())

# Run the spatial SIR simulation
for step in range(time_steps):
    new_population = population.copy()
    infected_y, infected_x = np.where(population == 1)
    for y, x in zip(infected_y, infected_x):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                # Calculate neighbor coordinates
                ny = y + dy
                nx = x + dx
                if 0 <= ny < 100 and 0 <= nx < 100:
                    if population[ny, nx] == 0:
                        if np.random.random() < beta:
                            new_population[ny, nx] = 1
    
    # Recovery process
    infected_indices = population == 1
    recover_mask = np.random.random(population.shape) < gamma
    new_population[infected_indices & recover_mask] = 2
    population = new_population
    
    if (step + 1) in time_points:
        snapshots.append(population.copy())

#plot the result
fig, axes = plt.subplots(2, 2, figsize=(4, 4), dpi=150)
axes = axes.flatten()
for idx, t in enumerate(time_points):
    ax = axes[idx]
    im = ax.imshow(snapshots[idx], cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
    ax.set_title(f'Time step = {t}')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
plt.colorbar(im, ax=axes, label='State: 0=Susceptible, 1=Infected, 2=Recovered', shrink=0.8)
plt.tight_layout()
plt.savefig("spatial_SIR_evolution.png", dpi=300)
plt.show()