# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm  # Import colormap module as suggested

#define the basic variables of the model
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
vax_rates = np.arange(0, 1.1, 0.1)

#Store the infection curve
infection_curves = []

for vax_rate in vax_rates:
    # Initialize population
    V = int(N * vax_rate)
    I = 1
    S = max(N - V - I, 0) # Prevent negative S from causing errors
    R = 0
    arr_I = [I]
    # Time loop (core simulation logic, same as original SIR model)
    for _ in range(time_steps):
        # Calculate force of infection
        infection_rate = beta * I / N
            
        # Prevent negative S from causing errors
        if S <= 0:
            new_infected = 0
        else:
            new_infected = np.random.choice([0, 1], S, p=[1 - infection_rate, infection_rate]).sum()
        new_recover = np.random.choice([0, 1], I, p=[1 - gamma, gamma]).sum()
        S -= new_infected
        I += new_infected
        I -= new_recover
        R += new_recover
        arr_I.append(I)
    infection_curves.append(arr_I)

#plot the result
plt.figure(figsize=(6, 4), dpi=150)
colors = cm.viridis(np.linspace(0, 1, len(vax_rates)))
for i, (vax_rate, curve) in enumerate(zip(vax_rates, infection_curves)):
    plt.plot(curve, color=colors[i], linewidth=2, label=f"{int(vax_rate*100)}%")
plt.title("SIR model with different vaccination rates", fontsize=14)
plt.xlabel("time", fontsize=12)
plt.ylabel("number of people", fontsize=12)
plt.legend()  # Shows the percentage labels
plt.savefig("SIR_vaccination.png", dpi=300)
plt.show()