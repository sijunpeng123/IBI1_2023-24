# import necessary l i b r a r i e s 
import numpy as np
import matplotlib.pyplot as plt

population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1

plt.figure ( figsize =(6 ,4) , dpi=150) 
plt.imshow ( population , cmap= 'viridis' , interpolation='nearest' )
N = 100  
beta = 0.3  
gamma = 0.05
# Define function to find the infected points and infect their neighbors
def infect_neighbors(population, beta):
    infected_indices = np.where(population == 1)  # Find indices of infected points
    infected_rows, infected_cols = infected_indices
    for index in range(len(infected_rows)):
        i, j = infected_rows[index], infected_cols[index]
        # Loop through the eight neighbors of the infected point
        for x in range(max(0, i-1), min(100, i+2)):
            for y in range(max(0, j-1), min(100, j+2)):
                # Skip the infected point itself and already infected or recovered individuals
                if (x, y) != (i, j) and population[x, y] == 0:
                    # Infect neighbors based on infection rate
                    if np.random.random() < beta:
                        population[x, y] = 1

# Define function to recover infected individuals
def recover(population, gamma):
    recovery_indices = np.where(population == 1)  # Find indices of infected points
    recovery_rows, recovery_cols = recovery_indices
    for index in range(len(recovery_rows)):
        i, j = recovery_rows[index], recovery_cols[index]
        # Recover infected individuals based on recovery rate
        if np.random.random() < gamma:
            population[i, j] = 2

# Create the figure
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Graph at time 0
axes[0, 0].imshow(population, cmap='viridis', interpolation='nearest')
axes[0, 0].set_title("Time 0")

# Graph at time 10
for _ in range(10):
    infect_neighbors(population, beta)
    recover(population, gamma)
axes[0, 1].imshow(population, cmap='viridis', interpolation='nearest')
axes[0, 1].set_title("Time 10")

# Graph at time 50
for _ in range(40):
    infect_neighbors(population, beta)
    recover(population, gamma)
axes[1, 0].imshow(population, cmap='viridis', interpolation='nearest')
axes[1, 0].set_title("Time 50")

# Graph at time 100
for _ in range(50):
    infect_neighbors(population, beta)
    recover(population, gamma)
axes[1, 1].imshow(population, cmap='viridis', interpolation='nearest')
axes[1, 1].set_title("Time 100")

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()