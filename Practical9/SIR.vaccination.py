# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm  # Import colormap module as suggested

# define the basic variables of the model
N = 10000
beta = 0.3
gamma = 0.05
vax_rates = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

#Store the infection curve
infection_curves = []

for vax_rate in vax_rates:
    R = int(N * vax_rate)
    I = 1
    S = N - R - I
    arr_I = [I]
    
    # Time loop
    for j in range(1000):
        # Calculate force of infection
        infection_rate = beta * I / N
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
colors = cm.viridis(np.linspace(0, 1, 10))
for i, (vax_rate, curve) in enumerate(zip(vax_rates, infection_curves)):
    plt.plot(curve, color=colors[i], linewidth=2, label=f"{int(vax_rate*100)}%")
plt.title("SIR model with different vaccination rates", fontsize=14)
plt.xlabel("time", fontsize=12)
plt.ylabel("number of people", fontsize=12)
plt.legend()
plt.savefig("SIR_vaccination.png", dpi=300)
plt.show()