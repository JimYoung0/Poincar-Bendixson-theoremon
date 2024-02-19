import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def rotating_vector_field(t, z, lambda_param):
    x, y = z
    dxdt = -y + lambda_param * (x**2 + y**2) * (1 - x**2 - y**2)
    dydt = x + lambda_param * (x**2 + y**2) * (1 - x**2 - y**2)
    return [dxdt, dydt]

lambda_param = 1.0
initial_conditions = [[0.01,0.01],[0.1, 0.1], [0.5, 0.5],[0.6, 0.6],[0.7,0.7], [0.9, 0.9]]
t_span = [0, 20]
t_eval = np.linspace(*t_span, 1000)

plt.figure(figsize=(8, 8))

for z0 in initial_conditions:
    sol = solve_ivp(rotating_vector_field, t_span, z0, args=(lambda_param,), t_eval=t_eval)
    plt.plot(sol.y[0], sol.y[1])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Rotating Vector Field for Different Initial Conditions')
plt.grid(True)
plt.show()
