import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Lotka-Volterra equations (Predator-Prey model)
def lotka_volterra(t, z, a, b, c, d):
    x, y = z
    return [x * (a - b * y), -y * (c - d * x)]

# Parameters I took by my favor
a, b, c, d = 0.1, 0.02, 0.3, 0.01

t = np.linspace(0, 200, 500)

initial_conditions = [
    (40, 9),  
    (20, 5),  
    (60, 15), 
    (50, 5),  
    (30, 20)  
]

plt.figure(figsize=(8, 6))

# This system here is easy to solve directly by Python
# Maybe finding a better method to solve a harder problem
for x0, y0 in initial_conditions:
    sol = solve_ivp(lotka_volterra, [t.min(), t.max()], [x0, y0], args=(a, b, c, d), t_eval=t)
    plt.plot(sol.y[0], sol.y[1], label=f'Initial: Prey={x0}, Predator={y0}')

plt.xlabel('Prey Population')
plt.ylabel('Predator Population')
plt.title('Phase Space for Various Initial Conditions')
plt.legend()
plt.grid(True)

plt.show()
