# import necessary l i b r a r i e s 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000
beta = 0.3
gamma = 0.05

vaccination_rates = np.linspace(0, 1, 11)

# making a graph
plt.figure(figsize=(6, 4), dpi=150)

for vaccination_rate in vaccination_rates:
    V = int(vaccination_rate * N)  # vaccinated people
    S = N - V - 1
    I = 1
    R = 0

    # creating I array
    I_arr = [I]

    # looping
    for _ in range(1000):
    
        if S > 0:
            infected = np.random.choice(range(2), S, p=[1 - min(beta * I / N, 1), min(beta * I / N, 1)])
            S -= np.sum(infected)
            I += np.sum(infected)

        # recovered people
        if I > 0:
            recovered = np.random.choice(range(2), I, p=[1 - gamma, gamma])
            I -= np.sum(recovered)
            R += np.sum(recovered)

        # I array append
        I_arr.append(I)

    # plotting the result
    plt.plot(I_arr, label=f'Vaccination rate: {vaccination_rate:.1f}', color=cm.viridis(vaccination_rate))

plt.xlabel('Time')
plt.ylabel('Number of infected people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()