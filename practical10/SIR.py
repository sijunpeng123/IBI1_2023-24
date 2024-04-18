# import necessary l i b r a r i e s 
import numpy as np
import matplotlib.pyplot as plt

# Define the basic variables of the model
# Total population
# Initial susceptible individuals
# Initial infected individuals
# Initial recovered individuals
# Infection rate
# Recovery rate
N = 10000
S = N - 1
I = 1
R = 0

beta = 0.3
gamma = 0.05

# Create arrays to track the evolution of the variables over time
S_arr = [S]
I_arr = [I]
R_arr = [R]

# Loop over 1000 time points
for _ in range(1000):
    # Susceptibles become infected
    infected = np.random.choice(range(2), S, p=[1 - beta * I / N, beta * I / N])
    S -= np.sum(infected)
    I += np.sum(infected)

    # Infecteds recover
    recovered = np.random.choice(range(2), I, p=[1 - gamma, gamma])
    I -= np.sum(recovered)
    R += np.sum(recovered)

    # Record the output of each time point
    S_arr.append(S)
    I_arr.append(I)
    R_arr.append(R)

# Plot the results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_arr, label='Susceptible')
plt.plot(I_arr, label='Infected')
plt.plot(R_arr, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model')
plt.legend()
plt.show()