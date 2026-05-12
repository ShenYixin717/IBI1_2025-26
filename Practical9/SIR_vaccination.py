# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# define the basic variables of the model
N = 10000
beta = 0.3
gamma = 0.05
# Add 1.0 to meet the requirement of 0%~100% vaccination rate
vax_rates = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# Store the infection curve for each vaccination rate
infection_curves = []

'''
Simulation process for each vaccination rate:
1. Calculate the number of vaccinated people (initial R)
2. Set initial susceptible, infected and recovered population
3. Run 1000 time steps of stochastic SIR simulation
4. Record the number of infected people at each time step
'''
for vax_rate in vax_rates:
    # Initialize population with vaccination
    R = int(N * vax_rate)
    # Ensure that we do not set an initial infected person when population is full
    if R < N:
        I = 1          # one initial infected person if possible
    else:
        I = 0          # if everyone is vaccinated, no infection
    S = N - R - I      # S will never be negative because R + I <= N
    
    arr_I = [I]
    
    # Time loop for 1000 steps
    for j in range(1000):
        # Calculate infection rate: beta * proportion of infected people
        infection_rate = beta * I / N
        # Stochastically determine new infected individuals
        if S > 0:
            new_infected = np.random.choice([0, 1], S, p=[1 - infection_rate, infection_rate]).sum()
        else:
            new_infected = 0
        # Stochastically determine new recovered individuals
        new_recover = np.random.choice([0, 1], I, p=[1 - gamma, gamma]).sum()
        
        # Update population numbers
        S -= new_infected
        I += new_infected
        I -= new_recover
        R += new_recover
        
        # Store infected number for plotting
        arr_I.append(I)
    infection_curves.append(arr_I)

'''
Plot the results:
1. Create figure with proper size and dpi
2. Use viridis colormap for different vaccination rates
3. Add title, labels and legend
4. Save and show the plot
'''
plt.figure(figsize=(6, 4), dpi=150)
colors = cm.viridis(np.linspace(0, 1, 11))
for i, (vax_rate, curve) in enumerate(zip(vax_rates, infection_curves)):
    plt.plot(curve, color=colors[i], linewidth=2, label=f"{int(vax_rate*100)}%")

# Add complete labels and title
plt.title("SIR model with different vaccination rates", fontsize=14)
plt.xlabel("time", fontsize=12)
plt.ylabel("number of infected people", fontsize=12)
plt.legend()

# Save figure correctly
plt.savefig("SIR_vaccination.png", dpi=300)
plt.show()