# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# define the basic variables of the model
S = 9999
I = 1
R = 0
N = 10000
beta = 0.3
gamma = 0.05

#create array for each variables
arr_S = [S]
arr_I = [I]
arr_R = [R]

'''
What I will need:
For each time step in 1000 steps:
    1. Calculate infection probability: infection_rate = beta * (I / N)
    2. Randomly select new_infected individuals from S using np.random.choice
    3. Randomly select new_recover individuals from I using np.random.choice
    4. Update the population numbers:
        S = S - new_infected
        I = I + new_infected - new_recover
        R = R + new_recover
    5. Append S, I, R to their respective arrays

'''

#coding of the time loop
for i in range(1000):
    infection_rate = beta * I / N
    new_infected = np.random.choice([0, 1], S, p=[1 - infection_rate, infection_rate]).sum()
    new_recover = np.random.choice([0, 1], I, p=[1 - gamma, gamma]).sum()
    S -= new_infected
    I += new_infected
    I -= new_recover
    R += new_recover
    arr_S.append(S)
    arr_I.append(I)
    arr_R.append(R)

#plot the result
data_S = np.array(arr_S)
data_I = np.array(arr_I)
data_R = np.array(arr_R)
plt.figure(figsize=(6,4), dpi=150)
plt.plot(data_S,color="blue",linewidth=2,label="susceptible")
plt.plot(data_I,color="orange",linewidth=2,label="infected")
plt.plot(data_R,color="green",linewidth=2,label="recovered")
plt.title("SIR model", fontsize = 14)
plt.xlabel("time",fontsize=12)
plt.ylabel("number of people",fontsize=12)
plt.legend()
plt.savefig("SIR",format="png")
plt.show()

